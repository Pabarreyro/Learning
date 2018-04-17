import {Triangle} from './../src/triangle.js';

describe('Triangle', function() {

  it('should test whether a Triangle has three sides', function(){
    var triangle = new Triangle(3,4,5);
    expect(triangle.side1).toEqual(3);
    expect(triangle.side2).toEqual(4);
    expect(triangle.side3).not.toEqual(6);
  });

  it('should correctly determine whether three lengths can be made into a triangle', function() {
    var triangle = new Triangle(12,3,3);
    expect(triangle.checkTriangle()).toEqual('not a triangle');
  });

  it('should correctly determine the type of triangle', function() {
    let testTriangle = new Triangle(2,3,4);
    expect(testTriangle.checkType()).toEqual('scalene');
  });
});
