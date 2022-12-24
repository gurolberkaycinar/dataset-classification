import {Routes} from '@angular/router';

import {DashboardComponent} from '../../dashboard/dashboard.component';
import {IconsComponent} from '../../icons/icons.component';
import {NotificationsComponent} from '../../notifications/notifications.component';

import {DatasetSamplesComponent} from "../../pages/dataset-samples/dataset-samples.component";
import {ModelDashboardComponent} from "../../pages/model-dashboard/model-dashboard.component";

export const AdminLayoutRoutes: Routes = [
  {path: 'dashboard', component: DashboardComponent},
  {path: 'icons', component: IconsComponent},
  {path: 'notifications', component: NotificationsComponent},
  {path: 'dataset-samples', component: DatasetSamplesComponent},
  {path: 'model-dashboard', component: ModelDashboardComponent}
];
