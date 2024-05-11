class Person {
    constructor(firstName, lastName, age, email) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
        this.email = email;
    }

    toString() {
        return ` ${this.firstName} ${this.lastName}, (Age: ${this.age}, Email: ${this.email} )`;
    }
}


const person = new Person('Mari', 'Petterson', 22, 'mp@gmail.com');


console.log(person.toString()); 