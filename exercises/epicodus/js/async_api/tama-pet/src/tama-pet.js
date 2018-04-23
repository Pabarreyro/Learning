let pet = {
  date: new Date(),
  tummy: 10,
  dirty: 0,
  sleep: false,
  hunger: function(){
    const hungerInterval = setInterval(()=> {
      this.tummy--;
      if (this.tummy == 0) {
        clearInterval(hungerInterval);
        return "Why did you kill me daddy?";
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
  sleep: function() {
    if(this.date.getHours() > 19 && this.date.getHours() < 9) {
      this.sleep = true;
    }
  },
  pooper: function(){
    const poopInterval = setInterval(()=> {
      this.dirty++;
      if (this.dirty > 5) {
        clearInterval(poopInterval);
        return "Why did you kill me daddy?";
      }
    }, 20000)
  }
};

export { pet }
