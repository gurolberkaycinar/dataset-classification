import {NgModule} from '@angular/core';
import {RouterModule} from '@angular/router';
import {CommonModule} from '@angular/common';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {AdminLayoutRoutes} from './admin-layout.routing';
import {ChartsModule} from 'ng2-charts';
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import {ToastrModule} from 'ngx-toastr';
import {DatasetSamplesComponent} from "../../pages/dataset-samples/dataset-samples.component";
import {ModelDashboardComponent} from "../../pages/model-dashboard/model-dashboard.component";
import {MatInputModule} from "@angular/material/input";
import {MatSelectModule} from "@angular/material/select";

@NgModule({
  imports: [
    CommonModule,
    RouterModule.forChild(AdminLayoutRoutes),
    FormsModule,
    ChartsModule,
    NgbModule,
    ToastrModule.forRoot(),
    MatInputModule,
    MatSelectModule,
    ReactiveFormsModule
  ],
  declarations: [
    DatasetSamplesComponent,
    ModelDashboardComponent,
  ]
})

export class AdminLayoutModule {
}
