export class Recipe {
  ingredients: Ingredient[] = [];
  preparation: Step[] = [];

  constructor(public title: string) {}

  addIngredient(ingredient){
    this.ingredients.push(ingredient);
  }

  addStep(step){
    this.preparation.push(step);
  }
}

class Ingredient {
  constructor(public name: string) {}
}

class Step {
  constructor(public description: string) {}
}
