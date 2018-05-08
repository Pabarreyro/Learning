import { Component, Input, Output, EventEmitter, OnInit } from '@angular/core';
import { AlbumService } from '../album.service';
import { Album } from '../album.model';


@Component({
  selector: 'app-edit-album',
  templateUrl: './edit-album.component.html',
  styleUrls: ['./edit-album.component.css'],
  providers: [AlbumService]
})
export class EditAlbumComponent implements OnInit {
  @Input() selectedAlbum;
  @Output() clickSender = new EventEmitter();

  constructor(private albumService: AlbumService) { }

  ngOnInit() {
  }

  beginUpdatingAlbum(albumToUpdate) {
    this.albumService.updateAlbum(albumToUpdate);

  }

  beginDeletingAlbum(albumToDelete) {
    if(confirm("Are you sure you want to delete this item from the inventory?")){
      this.albumService.deleteAlbum(albumToDelete);
    }
  }

  hideEdit() {
    this.clickSender.emit();
  }

}
