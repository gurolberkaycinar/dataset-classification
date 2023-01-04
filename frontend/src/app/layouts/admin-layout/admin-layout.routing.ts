import {Routes} from '@angular/router';
import {DatasetSamplesComponent} from "../../pages/dataset-samples/dataset-samples.component";
import {ModelDashboardComponent} from "../../pages/model-dashboard/model-dashboard.component";

export const AdminLayoutRoutes: Routes = [
  {path: 'dataset-samples', component: DatasetSamplesComponent},
  {path: 'model-dashboard', component: ModelDashboardComponent}
];
