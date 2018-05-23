import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import { AlbumService } from '../album.service';
import { Location } from '@angular/common';
import { Album } from '../album.model';
<<<<<<< HEAD
import { AlbumService } from '../album.service';
=======
>>>>>>> 48de9a7f1828967fb7ea17ee0cd76ad5306ca5f9
import { FirebaseObjectObservable } from 'angularfire2/database';

@Component({
  selector: 'app-album-detail',
  templateUrl: './album-detail.component.html',
  styleUrls: ['./album-detail.component.css'],
  providers: [AlbumService]
})
export class AlbumDetailComponent implements OnInit {
  albumId: string;
  albumToDisplay;

  constructor(
    private route: ActivatedRoute,
    private location: Location,
    private albumService: AlbumService) {}

  ngOnInit() {
    this.route.params.forEach((urlParameters) => {
      this.albumId = urlParameters['id'];
    });
    this.albumToDisplay = this.albumService.getAlbumById(this.albumId);
  }
}
