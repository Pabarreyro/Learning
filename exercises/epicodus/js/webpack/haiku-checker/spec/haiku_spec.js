import { checkLines, validateText } from './../src/validate.js';
import { Haiku } from './../src/haiku.js';

describe('Haiku', function() {
  let reusableText = "Haikus are easy.\nBut sumtimes they don't make sense.\nRefrigerator.";
  let testHaiku;

  beforeEach(function() {
    testHaiku = new Haiku(reusableText);
    testHaiku.countVowels();

  });

  it('should check text for unwanted charactors', function() {
    expect(validateText(reusableText)).toEqual(false);
  });

  it('should test whether a poem has three lines', function() {
    expect(checkLines(reusableText)).toEqual(2);
  });

  it('should split text into sentences at a new line break', function() {
    expect(testHaiku.lines.length).toEqual(3);
  });

  it('should count the number of vowels, vowel pairs, and qualifying ys in each sentence', function() {
    expect(testHaiku.vowelCounts).toEqual([6,10,5]);
  });

  it('should count the number of instances that a word ends with ie, e, but not le, in each sentence', function() {
    testHaiku.filterExclusions();
    expect(testHaiku.vowelCounts).toEqual([5,7,5]);
  });

  it('should determine if a poem is a Haiku', function() {
    testHaiku.filterExclusions();
    testHaiku.checkPass();
    expect(testHaiku.pass).toEqual(true);
  });

});
