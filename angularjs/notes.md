# AngularJS notes

## Introduction

AngularJSis a jasvaScript framekork written in JavaScript, intented to create web page easily,without too much JavaScript code. It is distributed as a single JavaScriptfile that can be imported via the ````script```` tag.

## Hello World

````html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hello world</title>
<script src="./angular.min.js"></script>
</head>
<body>
<h1>AnjularJS: Getting started</h1>
<p ng-app>AngularJS: {{'Hello world'}} how {{'is '+'everything?'}}</p>
</body>
</html>
````

### Explaination

* Import of the anglar js file

  The script tag is used to import the angular js file. We can either use the link to the web address of the angular js or downlod the file and import it.

The angular JS minimum file is located at: <https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js>

We can use the first option as follow:

````html
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
````

The second option is the one we used.

````html
<script src="./angular.min.js"></script>
````

We have downloaded the js min file and copied it in our current working directory, at as same level as our current html file.

* Inclusion of the ng-app directive

    ````ng-app```` is what we call an angular directive. It's attached to the p tag to tell it that we are going to use angular.So to use angularapplication, we need to attach the ng-app directive to the appropriate HTML tag(s).

* Use of angular js expressions
  We use ````double braces {{}}````.

{{}} allow us to use expressions, called angular expressions, that can be anny javascript type(number, boolean, string, array, etc).

By using double braces inside an HTML tag with or inside ng-app directive, web browser don't interpret it as a simple text, but as an angularJS expression.

### Another  angular directive: ng-init

The ng-init angular directive is used to initialize or re-assign an angularJS variable, using the ````=```` assignment operator.

Then the concerned variable wil be accessed anywhere in the anglarJS app.

In case of 2 or more initializations, we must seperate them with semoicolon(;)

The assignment can use a simple value or  an angularJS expression or an existing angularJS variable

#### Examples of use

````html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>init</title>
<script src="./angular.min.js"></script>
</head>
<body>
<h1>ng-init directive: overview</h1>

<div ng-app>
{{'Joy to the world'}}
<p ng-init="hello='Hello world!'">{{hello}}</p>
<p>Say hello to the world:<b >{{hello}}</b></p>

<p ng-init="age=20; firstname='Ezéchiel';
lastname='ADEDE'"> I'm {{firstname+" "+lastname}} and I'm {{age}} years old</p>
<p ng-init="age2=age+5">age2={{age2}}</p>
<p ng-init="age2=age2*5">{{age2}}</p>
</div>
</body>
</html>
````

## Expressions

We have previously talked about angularJS expression.

We already know that they can be used inside braces.

AngularJS expressions can also be used via the ng-bind angular directive

AngularJS expressions:

* spport data type such as numbers, string, booleans, arrays, objects, etc.
* support operations, such as concatenation(with string), arithmetic operators(+,*,-,/,%), comparaison operators(==,===,!=,<,>,<=,>=), etc
* can be used inside HTML tags
* can be as HTML attribute values

### Examples of use of expressions

````html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Expressions</title>
<script src="./angular.min.js"></script>
</head>
<body ng-app>
<h1>AnjularJS expressions</h1>
<p >4*5+6-3=<b>{{4*5+6-3}}</b> <br></p>
<p >44/3=<b>{{45/3}}</b> <br></p>
<p >45%3=<b>{{45%3}}</b> <br></p>

<p ng-init="my_favourite='blue'" style="background-color:{{my_favourite}} ">A simple text on blue background</p>
<p ng-init="fruits=['orange','mango','bananas','apple']">{{fruits}}</p>

<p>My second favourite frit is {{fruits[1]}}</p>
<p ng-init="marks={maths:15,english:20}">{{marks}}</p>

<div ng-app="" ng-init="quantity=3;cost=5">

<p>Total in dollar: {{ quantity * cost }}</p>
<p>quantity:<b ng-bind="quantity"></b></p>
<p>{{45<=2}} </p>
<p>{{45!=45}} {{true}} {{!false}}</p>
</div>

</body>
</html>
````

## Module

Module are created and loaded inside a script tag that's inside the body one.

### Create a module

An angularJS module defines an application. It's a container for the differents parts of an application, such as controllers, services, components, etc.

````js
angular.module('moduleName',dep)
````

* moduleName is the name of the module to create
* dep is an array of strings that represents the list of modules the module to create depends on.
  * dep is [] in case of no module dependency

### Load a module

To load an existing angular module:

````js
var app=angular.module('myApp')
````

* myApp is the name of the module to load.

#### Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AngularJS modules</title>
<script src="../angular.min.js"></script>
<script >
    //creation of the module
    let app=angular.module('myApp',[]);
    //app contains the module created
    //load for use
    let myApp=angular.module('myApp');
</script>
</head>
<body>
<h1>AngularJS modules</h1>
<p ng-app="myApp">{{'Use of the previously creted method'}}</p>
</body>

</html>
```

The script tag for module canbe put even after the body tag.

## Built-in directives

An angularJS directive is an HTML attribute that modify the default behaviour of the HTML tag it's applied(attached) to.

As an HTML attribute, it can hava a value or not.

AngularJS provides several built-in directives.

AngularJS built-in directives start with ````ng-````.

We have for example talked about:

* ng-app: the angularJS built-in directory that initialize an angularJS application; a value can be assigned(or not) to specify an application module
* ng-init: a directive used to initialize an angularJS variable
* ng-bind: an alternative to the braces expresssions of angularJs

## Data binding

Data binding in angularJS is the way used to share data between differents parts of an angularJS application.

There are two ways to bind data in angularJS: the one-way data binding and the two-ways data binding.

### One-way data binding

An angularJS data or expression is bound to an HTML elemenent. Whenever the concerned data or expression changes, the content of the concerned HTML element(s) change.

Data binding can be done using the angularJS braces or the angularJS directive ng-bind

### Two-ways data binding

In that case, an HTML element, typically an input element is bound to a data of the angularJS application. The value of the model changes no matter when the content of the concerned HTML element changes. Reciprocally, every time the model's value change, the HTML concerned element(s)'s content changes to.

That way of data binding can be used using the ng-model directive

### Examples: data binding

````html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Data binding</title>
<script src="../angular.min.js"></script>
</head>

<body ng-app>
<h1>Data binding</h1>
<h2>One-way data binding</h2>
<h3>Using braces</h2>
    <p ng-init="age=28" >I'm {{age}} years old</p>
<h3>Using ng-bind</h3>
<p>I'm <b ng-bind="age"></b> years old</p>


<h2>Two-ways data binding(ng-model)</h2>
<input type="text" ng-model="name"/> <b>{{name}}</b>
</body>

</html>
````

The difference between these data binding approches is that the first one is unidirectional whereas the second one is bidirectional.

## Controllers

A controller is a part of an angularJS app that controls the data ofthe application. It's a javaScript regular object, that's to say an unordered collection of key-value pairs where keys are string and values are any data type including functions.

An app controller belongs to a module of the app.

To create a controller, we first of all nedd to create or load the concerned modle and then use the controllermethod to create it.

### Controller creation and use: Example

````html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <script src="../angular.min.js"></script>
    <title>AngularJS controllers</title>
</head>
<body ng-app="myApp" >
<h1>AngularJS controllers</h1>
<div ng-controller="personCtrl">
<p >Personal informations:
    <div>Firstname: <b ng-bind="firstname"></b></div>
    <div>Lastname: <b>{{lastname}}</b></div>
    <div>Age: <b ng-bind="age"></b></div>
</p>
<p>{{describe()}}</p>
</div>

<div ng-controller="personCtrl">
    <p ng-bind="describe()"></p>
<input ng-model="tel"  type="tel" placeholder="Your phone number"><br>
<p>My phone number is {{tel}}</p>
</div>

</body>
<script>
    let app=angular.module('myApp',[]);
    app.controller('personCtrl',function($scope){
        //thre variables are available
        $scope.firstname="Ezéchiel";
        $scope.lastname="ADEDE";
        $scope.age=20;
        $scope.tel=95824746;
        //a function that describes a person
        $scope.describe=function(){
            return "I'm "+$scope.firstname+' '+
            $scope.lastname+" and I'm "+
            $scope.age+ " years old";
        };
    });
</script>
</html>
````

#### Controller creation and use: explaination

In the previous example, we se the controller method to create a controller. We pass as arguments to that method two arguments:

* a string, that represent the name of the controller, 'personCtrl' in our case
* a function in which we expose the data via the $scope parameter.

The $scope parameter represents the model. It allows to expose the available data such as the variables and the function, to the controller, and then it'll e accessible by the view.

To access the data inside our view, we first of all use the ng-controller directive with as value, the name of the controller, 'peronCtrl' in our case.

### The $rootScope

We can access our application data everywhere in our angularJS application with as controller name, the name of the concerned controller. That's possible own to the $scope variable passed as parameter to the function during the controller creation. For example in we cannot access any data of our person controller outide our ````<div ng-controller="personCtrl">````

There is another variable with a larger scope that make app data, meaning everywhere in any HTML tag with ng-app directive available everywhere in our angularJS app. It's the $rootScope. Consequently, Wherever we access a data whith the same identifier in $scope and $rootScope, the one of $scope will be used, as having a lower scope.

### $rootScope example

````html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <script src="../angular.min.js"></script>
    <title>AngularJS $scope and $scopeRoot</title>
</head>
<body ng-app="myApp" >
<h1>$scope and $scopeRoot</h1>
<div ng-controller="myCtrl">
<p> My favourite color:{{favouriteColor}}</p>
</div>

<div>
    <p> My favourite color:{{favouriteColor}}</p>
</div>
</body>
<script>
    let app=angular.module('myApp',[]);
    app.controller('myCtrl',function($scope){

        $scope.favouriteColor='blue';

    });
    app.run(function($rootScope){
    //alert('Hello');
    $rootScope.favouriteColor='yellow';

    })
</script>
</html>
````

## More about angularJS  directives

We made an overview about angularJS built-in directive.

Now we'll learn more examples of angularJS directives.

Here is the a classified list of some angularJS built-in directives.

| Directive Class | Directive Name | Explanation |
|---|---|---|
| Data Binding Directives | ngBind | Binds the text content of an HTML element to an expression in the current scope. |
| | ngBindHtml | Binds the innerHTML of an HTML element to an expression in the current scope. |
| | ngBindTemplate | Binds the template of an HTML element to an expression in the current scope. |
| | ngModel | Binds the value of an input, select, or textarea element to a property in the current scope, providing two-way data binding. |
| | ngModelOptions | Configures how the ngModel directive interacts with the HTML element. |
| Event Directives | ngClick | Executes an expression when the element is clicked. |
| | ngDblClick | Executes an expression when the element is double-clicked. |
| | ngMouseDown | Executes an expression when the mouse button is pressed down on the element. |
| | ngMouseUp | Executes an expression when the mouse button is released on the element. |
| | ngMouseOver | Executes an expression when the mouse cursor moves over the element. |
| | ngMouseLeave | Executes an expression when the mouse cursor leaves the element. |
| | ngMouseEnter | Executes an expression when the mouse cursor enters the element. |
| | ngMouseLeave | Executes an expression when the mouse cursor leaves the element. |
| | ngKeyDown | Executes an expression when a key is pressed down. |
| | ngKeyUp | Executes an expression when a key is released. |
| | ngKeyPress | Executes an expression when a key is pressed and released. |
| | ngSubmit | Executes an expression when the form is submitted. |
| | ngFocus | Executes an expression when the element gains focus. |
| | ngBlur | Executes an expression when the element loses focus. |
| | ngCopy | Executes an expression when the content is copied. |
| | ngCut | Executes an expression when the content is cut. |
| | ngPaste | Executes an expression when the content is pasted. |
| | ngTouchstart | Executes an expression when a touch event starts. |
| | ngTouchmove | Executes an expression when a touch event moves. |
| | ngTouchend | Executes an expression when a touch event ends. |
| | ngTouchcancel | Executes an expression when a touch event is canceled. |
| Structural Directives | ngIf | Conditionally includes or removes an element from the DOM based on an expression. |
| | ngSwitch | Conditionally renders one of multiple possible elements based on an expression. |
| | ngSwitchWhen | Specifies a case for the ngSwitch directive. |
| | ngSwitchDefault | Specifies a default case for the ngSwitch directive. |
| | ngRepeat | Iterates over an array or object and generates the element for each item. |
| | ngInclude | Includes an external HTML file into the current template. |
| | ngView | Renders a template based on the current URL route. |
| | ngClass | Adds or removes CSS classes to an element based on an expression. |
| | ngClassEven | Adds or removes CSS classes to an element if its index is even. |
| | ngClassOdd | Adds or removes CSS classes to an element if its index is odd. |
| | ngStyle | Sets CSS styles to an element based on an expression. |
| | ngDisabled | Conditionally disables an element based on an expression. |
| | ngReadonly | Conditionally sets the "readonly" attribute of an element based on an expression. |

### Examples of use of built-in directives

## Directive creation

## Filters

## Components

A component is a widget, piece of HTML code that can be re-used in several places of our web application.

### create and use component

Components are defined on angular modules.

To create a component on a module:

1.We can first of all load the moule:

````js
var app=angular.module('myApp')
````

2.then create the component

````js
app.component('comp',{})
````

* comp represents the name of the component
* {} is an object. It contains key value pairs that describe the component to create.

Components are using simply as HTML tags.

````html
<comp><comp>
````

### Rules for naming a component

### Details on angular components

During creation, we can specify a template for a component, using the key ````template```` and a string as it's value.

````js
app.component('helloWorld',{
    template:'<strong>Hello world!</strong>'
});
````

Usage:

````html
<hello-world><hello-world>
````

We can add parameter to a component using the ````bindings```` key. Then, it will be used as an attribute during usage.

The ````bindings```` key has as value an object which name is the identifier of the parameter and value represents the type of the parameter. For example, the value '@' specifies a string.

We can refer that parameter in the template (for example), using ````$ctrl.param```` where param is the identifier of the parameter.

````js
app.component('hello',{
    template:'Hello<strong>$ctrl.name</strong>',
    bindings:{name:'@'}

});
````

We can use the ````controller```` key to specify a controller to a component. It's value is a function.

$onInit can be used inside a controller. It's a function that will be executed at the initializing of the component.

````js
````

That can be useful during access to a parameter passed to the component inside the controller.

````js
````

The key ````controllerAs```` can be used to specify an alternative name(a string as value) for the controller.

The default value of ````controllerAs```` is $ctrl if none is specified.

Note: ctrl stands for controller.

The ````require```` key is used to make the componed access another component.

Not that we assess the parent only inside the $onInit function in the controller.

````js
app.component('',{
    require:{
    parent:'^parentComponent'
    },
    controller:{
        this.$onInit=function(){
            this.parent.foo()
        }
    }
})
````

* 2 or many parameters to component
* type of parameter
* rules for naming parameter

## Create custom directives

### Getting started

### Values of ddo

### Directive decorator

### Directive with isolated scope

### Nesting directives: require

## Angular project structure

## Constants

<https://www.w3schools.com/angular/angular_ref_directives.asp>
