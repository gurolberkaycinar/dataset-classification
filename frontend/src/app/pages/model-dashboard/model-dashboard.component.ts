import {Component, ElementRef, OnInit, QueryList, ViewChild, ViewChildren} from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-model-dashboard',
  templateUrl: './model-dashboard.component.html',
  styleUrls: ['./model-dashboard.component.css']
})
export class ModelDashboardComponent implements OnInit {
  accuracy: number
  precision: number
  recall: number
  selectedDataset: string
  selectedAlgorithm: string
  testPercentage: number
  labelColumn: string
  @ViewChild("oneItem") oneItem: any;
  @ViewChildren("count") count: QueryList<any>;

  constructor(private httpClient: HttpClient, private elRef: ElementRef) {
  }

  ngOnInit(): void {
    // this.initCharts();
  }

  onClickDatasetButton(selectedDataset: string) {
    this.selectedDataset = selectedDataset
  }

  onClickAlgorithmButton(selectedAlgorithm: string) {
    this.selectedAlgorithm = selectedAlgorithm
  }

  onClickStart() {
    this.updateCharts()
  }

  counterFunc(end: number, element: any, duration: number) {
    let range, current: number, step, timer;

    range = end - 0;
    current = 0;
    step = Math.abs(Math.floor(duration / range));

    timer = setInterval(() => {
      current += 1;
      element.nativeElement.textContent = current;
      if (current == end) {
        clearInterval(timer);
      }
    }, step);
  }

  animateCount() {
    let _this = this;

    let single = this.oneItem.nativeElement.innerHTML;

    this.counterFunc(single, this.oneItem, 7000);

    this.count.forEach(item => {
      _this.counterFunc(item.nativeElement.innerHTML, item, 2000);
    });
  }

  private updateCharts() {
    let algorithm: string
    switch (this.selectedAlgorithm) {
      case 'Naive Bayesian':
        algorithm = 'naive_bayes'
        break;
      case 'KNN':
        algorithm = 'naive_bayes' // TODO: KNN
        break;
    }

    // this.httpClient.get<any>(`http://127.0.0.1:5000/datasets/${this.selectedDataset}`)
    //   .subscribe(response => {
    //     // this.labelColumn = response.tableHeaders
    //     // this.tableValues = response.tableValues
    //   })

    this.httpClient.post<any>(`http://127.0.0.1:5000/classification/${algorithm}/${this.selectedDataset}`
      , {
        test_percentage: this.testPercentage,
        label_column: this.labelColumn
      })
      .subscribe(response => {
        console.log(response)
        this.accuracy = response.accuracy
        this.precision = response.precision
        this.recall = response.recall
        this.animateCount()
      })
  }
}
