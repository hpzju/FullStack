class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greeting() {
    console.log(`My name is ${this.name}, and I'm ${this.age} years old!`);
    console.log(
      `Module Wrap Functions:
       __dirname is ${__dirname}; 
       __filename is ${__filename}`
    );
  }
}

module.exports = Person;
