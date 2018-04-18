import { checkLines } from './../src/project.js';
import { splitSentences } from './../src/project.js';
import { countVowels } from './../src/project.js';
import { countWordsEndingE } from './../src/project.js';
import { updateVowelCount } from './../src/project.js';

describe('Haiku', function() {
  let reusableText = "Haikus are easy.\nBut sometimes they don't make sense.\nRefrigerator.";

  it('should test whether a poem has three lines', function() {
    expect(checkLines(reusableText)).toEqual(2);
  });

  it('should split text into sentences at a new line break', function() {
    expect(splitSentences(reusableText).length).toEqual(3);
  });

  it('should count the number of vowels, vowel pairs, and qualifying ys in each sentence', function() {
    expect(countVowels(reusableText)).toEqual([6,11,5]);
  });

  it('should count the number of instances that a word ends with ie, e, but not le, in each sentence', function() {
    expect(countWordsEndingE(reusableText)).toEqual([1,2,0]);
  });

  it('should subtract number of words that end in e from the number of vowels in the sentence', function() {
    expect(updateVowelCount(reusableText)).toEqual([5,9,5]);
  });
});
