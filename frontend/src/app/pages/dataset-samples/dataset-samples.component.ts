import { Component, OnInit } from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-dataset-samples',
  templateUrl: './dataset-samples.component.html',
  styleUrls: ['./dataset-samples.component.css']
})
export class DatasetSamplesComponent implements OnInit {

  tableHeaders: string[]
  tableValues: string[]
  selectedDataset: string;
  prettierSelectedDataset: string;
  constructor(private httpClient: HttpClient) { }

  ngOnInit(): void {
    this.updateTable()
  }

  onClickButton(selectedDataset: any, prettierSelectedDataset: string) {
    this.selectedDataset = selectedDataset
    this.prettierSelectedDataset = prettierSelectedDataset
    this.updateTable()
  }

  private updateTable() {
    this.httpClient.get<any>(`http://127.0.0.1:5000/datasets/${this.selectedDataset}`)
      .subscribe(response => {
        this.tableHeaders = response.tableHeaders
        this.tableValues = response.tableValues
      })
  }
}
