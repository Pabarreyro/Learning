import { pet } from './../src/tama-pet.js';

describe('TamaPet', function() {
  let testPet = pet;

  beforeEach(function() {
    jasmine.clock().install();
    testPet.hunger();
    testPet.pooper();
  });

  afterEach(function() {
    jasmine.clock().uninstall();
    testPet.hunger();
    testPet.pooper();
  });

  it('should create an initial pet', function() {
    expect(testPet.tummy).toEqual(10);
  });
  it('should die when tummy is empty', function() {
    jasmine.clock().tick(10001);
    expect(testPet.tummy).toEqual(0);
  });
  it('should after 10 seconds if not fed', function() {
    jasmine.clock().tick(10001);
    expect(testPet.petCemetery()).toEqual(true);
  });
  it('should get dirty every 20 seconds', function() {
    jasmine.clock().tick(20001);
    expect(testPet.dirty).toEqual(1);
  });
  it('should want to play only when it fed', function() {
    jasmine.clock().tick(7001);
    expect(testPet.play()).toEqual(false);
  });
  it('should sleep when hours reach between 19 and 9', function() {
    testPet.date.setHours(20);
    console.log(testPet.date);
    testPet.bedtime();
    expect(testPet.sleep).toEqual(true);
  });
  it('should make make pet bigger every hour', function() {
    testPet.birthday();
    jasmine.clock().tick(3600001);
    expect(testPet.age).toEqual(1);
  });
});
