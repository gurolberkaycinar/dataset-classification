import {Component, ElementRef, OnInit, QueryList, ViewChild, ViewChildren} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {FormControl, FormGroup, Validators} from "@angular/forms";

@Component({
  selector: 'app-model-dashboard',
  templateUrl: './model-dashboard.component.html',
  styleUrls: ['./model-dashboard.component.css']
})
export class ModelDashboardComponent implements OnInit {
  accuracy: number = 0
  precision: number = 0
  recall: number = 0
  selectedDataset: string = 'Wine'
  headers: string[] = []
  selectedAlgorithm: string = 'Knn'
  trained: boolean = false;
  trainForm: FormGroup;
  predictForm: FormGroup;
  trainedDataset: string;
  predictedValue: string = null;
  gradientFill
  ctx
  canvas
  chartColor
  gradientStroke
  featureImportanceChartData: Array<any>
  featureImportanceChartLabels: Array<any>
  featureImportanceChartColors: Array<any>
  constructor(private httpClient: HttpClient) {
  }

  ngOnInit(): void {
    this.getHeaders();
    this.initTrainForm()
  }

  onClickTrain() {
    this.updateCharts()
  }

  onClickPredict() {
    const body = {
      features: this.predictForm.value,
      label: this.trainForm.get('label_column').value
    };
    let algorithm: string
    switch (this.selectedAlgorithm) {
      case 'Naive Bayesian':
        algorithm = 'naive_bayes'
        break;
      case 'Knn':
        algorithm = 'knn'
        break;
    }
    this.httpClient.post<any>(`http://127.0.0.1:5000/prediction/${algorithm}`
      , body)
      .subscribe(response => {
        console.log(response)
        this.predictedValue = response;
      })
  }

  isKnn(): boolean {
    return this.selectedAlgorithm == 'Knn'
  }

  isTrainFormInvalid(): boolean {
    return this.trainForm.invalid;
  }

  isPredicted(): boolean {
    return this.predictedValue != null;
  }

  onDatasetChange(selectedDataset: string) {
    this.selectedDataset = selectedDataset;
    this.selectedDataset != this.trainedDataset ? this.trained = false : this.trained = true;
    this.getHeaders();
  }

  onAlgorithmChange(selectedAlgorithm: string) {
    this.selectedAlgorithm = selectedAlgorithm;
    switch (selectedAlgorithm) {
      case 'Knn':
        this.trainForm.get('neighbour_count').setValidators(Validators.required)
        this.trainForm.get('distance_order').setValidators(Validators.required)
        break;
      case 'Naive Bayesian':
        this.trainForm.get('neighbour_count').clearValidators()
        this.trainForm.get('distance_order').clearValidators()
        break;

    }
    this.trainForm.get('neighbour_count').updateValueAndValidity()
    this.trainForm.get('distance_order').updateValueAndValidity()
  }

  private updateCharts() {
    let algorithm: string
    switch (this.selectedAlgorithm) {
      case 'Naive Bayesian':
        algorithm = 'naive_bayes'
        break;
      case 'Knn':
        algorithm = 'knn'
        break;
    }

    const body = this.trainForm.value;
    this.httpClient.post<any>(`http://127.0.0.1:5000/classification/${algorithm}/${this.selectedDataset}`
      , body)
      .subscribe(response => {
        this.accuracy = response.accuracy.toFixed(4)
        this.precision = response.precision.toFixed(4)
        this.recall = response.recall.toFixed(4)
        this.initPredictForm();
        this.trained = true;
        this.initFeatureImportanceGraph();
        this.predictedValue = null;
      })
  }

  private getHeaders() {
    this.httpClient.get<any>(`http://127.0.0.1:5000/datasets/${this.selectedDataset}`)
      .subscribe(response => {
        this.headers = response.tableHeaders
      })
  }
  private initTrainForm() {
    this.trainForm = new FormGroup({
      test_percentage: new FormControl(null, Validators.required),
      label_column: new FormControl(null, Validators.required),
      neighbour_count: new FormControl(),
      distance_order: new FormControl()
    });
  }

  private initPredictForm() {
    const formControls = {};
    this.headers.forEach(header => {
      formControls[header] = new FormControl();
    });
    this.predictForm = new FormGroup(formControls);
  }

  initFeatureImportanceGraph() {
    let params = {
      dataset: this.selectedDataset,
      label_column: this.trainForm.get('label_column').value,
      type: 'list'
    }
    console.log("--------------------------------------------------------")
    this.httpClient.get<any>(`localhost:5000/feature-importance`, { params: params } )
      .subscribe( response => {

        console.log(response);
      })
    // this.chartColor = "#FFFFFF";
    // this.canvas = document.getElementById("featureImportanceChart");
    // this.ctx = this.canvas.getContext("2d");
    //
    // this.gradientStroke = this.ctx.createLinearGradient(500, 0, 100, 0);
    // this.gradientStroke.addColorStop(0, '#80b6f4');
    // this.gradientStroke.addColorStop(1, this.chartColor);
    //
    // this.gradientFill = this.ctx.createLinearGradient(0, 200, 0, 50);
    // this.gradientFill.addColorStop(0, "rgba(128, 182, 244, 0)");
    // this.gradientFill.addColorStop(1, "rgba(255, 255, 255, 0.24)");
    //
    //
    //
    // this.gradientFill = this.ctx.createLinearGradient(0, 200, 0, 50);
    // this.gradientFill.addColorStop(0, "rgba(128, 182, 244, 0)");
    // this.gradientFill.addColorStop(1, "rgba(255, 255, 255, 0.24)");
    //
    //
    //
    //
    // this.featureImportanceChartData = [
    //   {
    //     label: "Active Countries",
    //     pointBorderWidth: 2,
    //     pointHoverRadius: 4,
    //     pointHoverBorderWidth: 1,
    //     pointRadius: 4,
    //     fill: true,
    //     borderWidth: 1,
    //     data: [80, 99, 86, 96, 123, 85, 100, 75, 88, 90, 123, 155]
    //   }
    // ];
    // this.featureImportanceChartColors = [
    //   {
    //     backgroundColor: this.gradientFill,
    //     borderColor: "#2CA8FF",
    //     pointBorderColor: "#FFF",
    //     pointBackgroundColor: "#2CA8FF",
    //   }
    // ];
    // this.featureImportanceChartLabels = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    //
  }
}
