<?php
/*
Laravel is a Model-View-Controller (MVC) web-development framework written in php

you should modify the code in routes.php file

Sometimes in the web application,you may need to capture the parameter passed with the URL.

you can capture the parameters in routes.php file in two ways:

1. Require Parameter

2. Optional Parameter

route parameters are encapsulated within {} with alphabets inside

example capturing the user-id:

Route::get('emp/{id}',function($id){

    return 'Emp '.$id;
});

Optional Parameter:

Suppose you want to specify the route parameter occasionally, in order to achieve this, you can make the route parameter optional.

you may do so by placing a '?' mark after the parameter name:

Route::get('emp/{id?}',function($id){

    return 'User' .$id;
    
});

Named routes allow the convenient generation of URLs or redirects for specific routes.

The chaining of routes can be specified using name() method onto the route definition as:

Route::get('user/profile','UserController@showProfile')->name('profile');

The user controller will call for the function showProfile with parameter as a profile. 
The parameters use the ame method onto the route definition.

Controllers are another essential feature provided by Laravel.

Controllers are used to define the actions that can be performed on the web application.

Initially, we were handling the request logic in the form of 
closures in route files; now, in place of using closures in route 
files, we use controller classes. 
A controller's job can be boiled down to this simple 
definition: 
It receives the request from the client and returns a response 
to the client. 

Controllers are meant to group associated request handling logic within a single class.

In your Laravel project,they are stored in the app/Http/Controllers' directory.

A controller does the same thing as a route definition with an anonymous function set as the "action" when that route is hit.

F:\panag\Documents\my-laravel-project\app\Http\Controllers>php artisan make:controller <Controller.php> --plain 

This will eventually make a plain constructor since you are passing the argument --plain

Hello I am calling from routes.php 
The created controller can be called from routes.php file 
using this syntax as mentioned below: 
Route::get('base URI','controller@method'); 
Now execute the below command to create UserController. 
php artisan make:controller UserController --plain 
After successful execution, you will receive the output as 
shown in the image above. 

Middleware acts as a bridge between a request and a user.

In Laravel, middleware is used to perform some action before and after a request is processed by the application.

It provides the method to filter HTTP requests that get entered into your project.

If the user's request is authenticated then the request is sent to the backend.

If the user's request isn't authenticated,then middleware will redirect the user to the login screen.

You can assign controllers to middlewares to route in the 
route files of your project using the command below: 
Route::get('profile', 
'AdminController@show')->middleware('auth'); 
Here we are assigning auth middleware to UserController in 
profile route. 
Middleware methods from the controller help to easily 
assign middleware to the controller's action and activity. 

<?php 
Controller's constructor 
namespace App\Http\Controllers; 
use Illuminate\Http\Request; 
use App\Http\Requests; 
use App\Http\Controllers\Controller; 
class UserController extends Controller { 
public function _construct() { 
$this->middleware('auth'); 

Here we are assigning auth middleware using the 
middleware method in the UserController constructor. 

Using closures, controllers may allow Laravel developers to register middleware.

This provides a convenient way to define a middleware for a single controller without defining an entire middleware class:

    $this->middleware(function ($request,$next){

        
        return $next($request);
        
        }

    );

Often while making an application we need to perform 
CRUD (Create, Read, Update, Delete) operations. 
Laravel makes this job easy for you. 
This can be created quickly using the make:controller 
command (Artisan command) something like this: 
F:\panag\Documents\my-laravel-project>php artisan make:controller MyController 

Suppose,you may wish to create a controller that handles all HTTP requests for "password" stored by your application

Using the make:controller Artisan command, we can quickly create such a controller:

F:\panag\Documents\my-laravel-project>php artisan make:controller PasswordController --resource

The above code will pproduce a controller in app/Http/Controllers location with file name PasswordController.php
which will hold a method for all available resource tasks.

You can register a resourceful route to the controller:

Route::resource('password','PasswordController');

This particular, as well as single route declaration,produces various routes to manipulate or handle a variety of activities on the resource.

Implicit controllers allow developers to define a single route 
for handling multiple actions within the controller. 
You can define it in route.php file with Route:controller 
method as shown below. 
Route::controller('base 
URI','<class-name-of-the-controller>'); 
It is where your Implicit controller file will get stored: app/ 
Http/Controllers/lmplicitController.php. 

TABLE:

Verb 
GET 
POST 
GET 
GET 
PUT 
DELETE 
Path 
/user 
/user/add 
/users/{user} 
/users/{user} 
/users/{user} 
Action 
user list 
Add new user 
Get user 
Edit user 
Update user 
Delete user 
Route Name 
user.indcx 
uscr.ads 
user.show 
uscr.edit 
uscr.update 
user.destroy

Multiple resource controller 
Laravel developers also have the freedom to register 
multiple resource controllers at a time by passing an array to 
the resource method. 
Route::resources([ 
'password' => 'PasswordController', 
'username' => 'UsernameController' 
]);

VIEW:

Views contain the html code required by your application.

It separates the application logic and the presentation logic.

The location of view is inside the resources/views folder.

[poject_folder]/resources/views

While building an application it may be required to pass data to the view.

with() function:

Route::get('games',function(){
    $Contact=['ProgrammingHub','hub'];
    return with('games')->with('ProgrammingHub',$Contact);

});


compact() function:

Route::get('games',function(){
    $Contact=['ProgrammingHub','hub'];
    return view('games',compact('games'));

});


Blade Templates:

Blade is a PHP template engine.

Blade Templates are used to generate HTML code.

Blade Templates are stored inside the resources/views folder.

[project_folder]/resources/views

The Blade is a powerful templating engine in a laravel framework.

Unlike other popular PHP templating engines, Blade does not restrict you from using plain PHP code in your views

Blade view files use the .blade.php file extension and are typically stored in the resources/views directory.

The main advantage of using the blade template is that we can create the master template, which can be extended by other files.

A master layout is made which can be later on extended to other templates and reused on other blade template files easily.

The @yield directie is used to display the contents of a given section.

Extending a Layout

The @extends directive is used to extend the layout.

The @yield directive is used to display the contents of a given section.

The @section('content') defines the section of the content.

Control Statements in Blade Template 

In addition to template inheritance and displaying data, 
Blade also provides convenient short-cuts for common PHP 
control structures, such as conditional statements and loops. 

A condition in Laravel starts with a special character '@'. 

if statement:


<html>
<body>
@if(($id) == 1)
    I have one project
@elseif(($id) == 2)
    I have two projects
@elseif(($id) >= 3)
    I have more than two projects
@else
    I have no projects
@endif
</body>
</html>

@unless directive

The @unless directive is used to display the contents of a given section if the condition is false.

The @endunless directive is used to end the @unless directive.

The @empty directive is used to display the contents of a given section if the variable is empty.

The @endempty directive is used to end the @empty directive.

The @isset directive is used to display the contents of a given section if the variable is set.

The @endisset directive is used to end the @isset directive.

<html>
<body>
    @unless($id==1)
        Kindly sign in.
    @endunless
</body>
</html>

for loop in blade

<html>
<body>
value of i:
@for($i=0;$i<10;$i++)
    {{$i}}
@endfor
</body>
</html>


foreach loop in blade

<html>
<body>
@foreach($users as $user)
    {{$user}}
@endforeach
</body>
</html>


while loop in blade

<html>
<body>
@while($i<10)
    {{$i}}
@endwhile
</body>
</html>

switch statement in blade

<html>
<body>
@switch($id)
@case(1)
    I have one project
@break
@case(2)
    I have two projects
@break
@default
    I have no projects
@endswitch
</body>
</html>

Requests in Laravel:

Request is an object that contains all the information about the request.

HTTP request 

To retrieve an occurrence of the current HTTP request 
through dependency injection, you need to type-hint the 
Illuminate\Http\Request class on your controller system or 
method.
 
The Illuminate\Http\Request instance provides a variety 
of methods for examining the HTTP request for your 
application.

Retrieving the Request URI

To retrieve the URI of the current request,
you can use the getUri() method.

The "path" method is used to retrieve the requested URI.

So, if the incoming request is targeted at http://domain.com/foo/bar, the path method will return foo/bar: 

    $uri=$request->path();


if ($request->is('admin/*')){

    //
}

The 'is' method enables you to validate that the incoming request path meets a furnished or given pattern.

You can utilize the * character as a wildcard when appropriating the method as given above.

full URL 

You can use the URL method to recover or retrieve the full 
URL for the incoming request. 

$url = $request->url(); 

In retrieving the request method, the 'method' method will 
return the HTTP verb for the request. 

You can apply the 'isMethod' method to analyse that the 
HTTP verb matches a given string: 

$method = $request->method(); 

if ($request->isMethod('post')) { 

//

}

The input values can be easily retrieved in Laravel

Applying several uncomplicated methods, you may be able to access all of the user input from your Illuminate\Http\Request.

You do not need to worry about the HTTP verb used fo the request,as input is accessed in the same way for all verbs:

    $name=$request->input('username');



You may give or pass a default value as the second following argument to the input method.

This value will be returned if the requested input value is not present on the request:
    $name=$request->input('name','Lara');

"dot" notation to access the arrays:


    $name=$request->input('products.0.name');

you can call the input method outwardly any arguments to regain or retrieve all of the input values as an associative array:


    $input=$request->input();


Recovering a portion of the input data 

You can apply the only and except methods on laravel 
request objects if you demand to recover a subset of the 
input data.
 
Both of these methods will accept a single array or a 
dynamic list of arguments:
 
$input = $request->only(['firstname', 'lastname']); 
$input = $request->only('firstname', 'lastname'); 
$input = $request->except(['id_no']); 
$input = $request->except('id_no'); 

Determining if an input value Is present 

You may use the 'has' method to conclude if a value is 
already there on the request. 

The has method returns true if the value is present and is not 
an empty string: 

if ($request->has('name')) { 

	//
	
}

Determining if an input value Is present 

When delivered an array, the 'has' method will conclude if 
each of the particularized values is present: 

if ($request->has(['name', 'address'])) { 

//

}

HTTP Responses:

All routes and controllers should return some kind of response to be sent back to the user's browser.

Laravel provides several different ways to return responses

Responses can be sent either from route or from controller.

The most basic response: Returning a string :

Route::get('/basic_response',function(){

    return 'Hello World';

});

The given string will automatically be converted into an HTTP response by the framework.

Attaching headers to responses: header( ) 

Keep in mind that most response methods are chainable, 
allowing for the fluent building of responses. 

The response can be attached to headers using the header() 
method. 

We can also attach the series of headers as given below: 

return response($content,$status)
 
	->header('Content-Type', $type) 
	->header('X-Header-One', 'Header Value') 
	->header('X-Header-Two', 'Header Value'); 


JSON Response:

JSON Response can be sent using the json method.

The json method returns an instance of the Illuminate\Http\Response class.

The json method takes an array or an object as an argument.

The json method will automatically set the Content-Type header to application/json.

View response:

If you need control over the response status and headers, 
but also need to return a view as the response content,
you may use the view method:

return response()->view('hey',$data)->header('Content-Type',$type);

If you don't need to pass a custom HTTP status codeor custom headers,you may simply use the global view helper function.

File downloads:

The download method may be used to generate a response that forces the user's browser to download the file at the given path.

The download method accepts a filename as the second argument to the method, 
which will determine the file name that is seen by the user downloading the file.

HTTP headers:

Finally,you may pass an array of HTTP headers as the third argument to the method as:

return response()->download($pathToFile);

or

return response()->download($file, $name, $headers);

Redirections:

Redirect contains the proper headers needed to redirect the user to another URL.

There are various ways to generate a RedirectResponse instance.

The simplest method is to use the global redirect helper method:

Route::get('profile',function(){

    return redirect('home/profile');

});

Redirecting to Named Routes :

Named route is used to give a specific name to a route.

The name can be assigned using the "as" array key.

Route::get('user/dashboard',['as' => 'dashboard',function(){

    //

}]);

We have given the name dashboard to a route user/dashboard.

Route method 

To generate a RedirectResponse to a named route, you may 
use the route method:
 
return redirect()->route('login'); 

If your route has parameters, you may pass them as the 
second argument to the route method:
 
return redirect()->route('dashboard', [1]); 

Redirecting to Controller Actions 

Not only named routes but we can also redirect to controller 
actions. 

To do so, simply pass the controller and action name to the 
action method as: 

return redirect()->action('NameOfController@methodName') 

For example,
 
return redirect()->action('HomeController@index'); 


Parameter comes to a picture 

Of course, if your controller route requires parameters, 
you may pass them as the second argument to the action 
method:
 
return redirect()->action('NameOfController@methodName', 
[parameters]); 

For example, 

return redirect()->action('UserController@dashboard', [1]) 




*/
