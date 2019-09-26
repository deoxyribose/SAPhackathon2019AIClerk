import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PlayerComponent } from './components/player/players.component';

import {
  MatCardModule,
  MatButtonModule,
  MatProgressBarModule
} from '@angular/material';
import { FundamentalNgxModule, ImageModule, IconModule } from 'fundamental-ngx';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ScrollingModule } from '@angular/cdk/scrolling';
import { ApiService } from './api.service';
import { HttpClientModule } from '@angular/common/http';
@NgModule({
  declarations: [AppComponent, PlayerComponent],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    HttpClientModule,
    AppRoutingModule,
    MatCardModule,
    MatButtonModule,
    MatProgressBarModule,
    FundamentalNgxModule,
    ImageModule,
    ScrollingModule,
    IconModule
  ],
  providers: [ApiService],
  bootstrap: [AppComponent]
})
export class AppModule {}
