let pet = {
  date: new Date(),
  tummy: 10,
  dirty: 0,
  sleep: false,
  health: 20,
  age: 0,
  hunger: function(){
    const hungerInterval = setInterval(()=> {
      this.tummy--;
      this.health--;
      if (this.petCemetery() === true) {
        clearInterval(hungerInterval);
      }
    }, 1000)
  },
  petCemetery: function(){
    if (this.tummy > 0 && this.dirty < 10) {
      return false;
    } else {
      return true;
    }
  },
  play: function(){
    if (this.tummy > 5) {
      return true;
    } else {
      return false;
    }
  },
  bedtime: function() {
    if(this.date.getHours() > 19 || this.date.getHours() < 9) {
      this.sleep = true;
    }
  },
  pooper: function(){
    const poopInterval = setInterval(()=> {
      this.dirty++;
      this.health--;
      if (this.petCemetery === true) {
        clearInterval(poopInterval);
      }
    }, 4000)
  },
  birthday: function() {
    const ageInterval = setInterval(()=> {
      this.age++;
      if(this.petCemetery() === true) {
        clearInterval(ageInterval);
      }
    }, 60000)
  },
};

export { pet }
