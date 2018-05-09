import { Injectable } from '@angular/core';
import { Photo } from './photo.model';
import { AngularFireDatabase, FirebaseListObservable } from 'angularfire2/database';

@Injectable()
export class PhotoService {
  photos: FirebaseListObservable<any[]>;

  constructor(private angularfire: AngularFireDatabase) {
    this.photos = angularfire.list('photos');
   }

  addPhoto(newPhoto: Photo) {
    this.photos.push(newPhoto);
  }

  getPhotos(){
    return this.photos;
  }

  deletePhoto(selectedPhoto){
    this.getPhotoById(selectedPhoto.$key).remove();
  }

  getPhotoById(id: string){
    return this.angularfire.object('photos/'+id);
  }


}
