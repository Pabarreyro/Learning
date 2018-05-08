import { Injectable } from '@angular/core';
import { Album } from './album.model';
import { AngularFireDatabase, FirebaseListObservable } from 'angularfire2/database';

@Injectable()
export class AlbumService {
  albums: FirebaseListObservable<any[]>;

  constructor(private database: AngularFireDatabase) {
    this.albums = database.list('albums');
  }

  getAlbumById(albumId: string){
    return this.database.object('albums/' + albumId);
  }

  getAlbums() {
    return this.albums;
  }

  addAlbum(newAlbum: Album) {
    this.albums.push(newAlbum);
  }

  updateAlbum(localUpdatedAlbum){
    let albumEntryInFireBase = this.getAlbumById(localUpdatedAlbum.$key);
    albumEntryInFireBase.update({title: localUpdatedAlbum.title,
                                artist: localUpdatedAlbum.artist,
                                description: localUpdatedAlbum.description});
  }

  deleteAlbum(localUpdatedAlbum){
    let albumEntryInFireBase = this.getAlbumById(localUpdatedAlbum.$key);
    albumEntryInFireBase.remove();
  }

}
