import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CompletenessPipe } from './completeness.pipe';

import { AppComponent } from './app.component';
import { TaskListComponent } from './task-list/task-list.component';
import { NewTaskComponent } from './new-task/new-task.component';
import { EditTaskComponent } from './edit-task/edit-task.component';
import { NavbarComponent } from './navbar/navbar.component';


@NgModule({
  declarations: [
    AppComponent,
    TaskListComponent,
    NewTaskComponent,
    EditTaskComponent,
    CompletenessPipe,
    NavbarComponent
  ],
  imports: [
    BrowserModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
