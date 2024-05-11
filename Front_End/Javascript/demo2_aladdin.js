/ Synchronous (Sync) code
 
// console.log("start")
// for(let i = 1; i<=3; i++){
//     console.log(i)
// }
// console.log("end")
 
// Asynchronous (Async) code
 
// console.log("start")
// setTimeout(function(){
//     console.log("We are inside setTimeout")
// },1000)
// console.log("end")
 
// console.log("Start");
 
// const delay = (ms) => new Promise((resolve) => setTimeout(resolve,ms));
 
// delay(1000)
// .then(() => {
//     console.log("Inside promise")
// })
// .then (() => {
//     console.log("end")
// })
 
 
 
// var add = function(x, y) {
//     return x + y;
// }
 
// var add = (x, y) => x + y;
 
 
 
// // Traditional function:
// function Person() {
//     this.age = 0;
//     setInterval(function growUp(){
//         this.age++;     // 'this' does not refer to the Person object....leading to an error
//     }, 1000)
// }
 
// // Arrow function:
// function Person() {
//     this.age = 0;
//     setInterval(() =>{
//         this.age++;     // 'this' properly refers to the Person object
//     }, 1000)
// }
 
// console.log("Traditional Function: ");
// const array = [1, 2, 3, 4];
// const squares = array.map(function (x) {
//     return x*x;
// });
 
// console.log(squares)
 
// console.log("Arrow Function")
// const squaresArrow = array.map(x=> x*x);
// console.log(squaresArrow)
 
 
 
// class User {
//     constructor(firstName, lastName, email){
//         this.firstName = firstName;
//         this.lastName = lastName;
//         this.email = email;
//         this.loggedIn = false;
//     }
//     login(){
//         this.loggedIn = true;
//         console.log(`${this.firstName} has logged in`);
//     }
//     logout(){
//         this.loggedIn = false;
//         console.log(`${this.firstName} has logged out`);
//     }
// }
 
// let userOne = new User('John', 'Smith', 'email@email.com');
// let userTwo = new User('Marie', 'Curie', 'marie@email.com');
 
// userOne.login();
// userTwo.logout();
 
 
 
// class Person{
//     constructor(firstName, lastName){
//         this.firstName = firstName;
//         this.lastName = lastName;
//     }
 
//     get fullName(){
//         return `${this.firstName} ${this.lastName}`;
//     }
 
//     set fullName(value){
//         const parts = value.split(' ');
//         this.firstName = parts[0];
//         this.lastName = parts[1];
//         console.warn('Changed the name');
//     }
// }
 
// const p1 = new Person('John', 'Smith')
 
// console.log(p1.fullName);
// p1.fullName = "Bob Bobson";
// console.log(p1.fullName);
 
 
 
class UserService {
    constructor(uri){
        this.baseUri = uri;
    }
 
    static signUp(user){
        console.log("Registering user");
        console.log(user)
    }
 
    static signIn(email, password){
        console.log(`Logging in user with ${email} and password is: ${password}`)
    }
}
 
UserService.signUp({firstName: 'John', lastName:'Smith'})
UserService.signIn('john@email.com', 'pocahontas123')