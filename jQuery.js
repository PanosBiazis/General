/* syntax:

    $(selector).action()

    $ sign to defines/access jQuery

    (selector) to find HTML elements

    .action() to perform an action on the elements

    example:

    $(this).hide() : hides the current element

    $("p").hide() : hides all <p> elements

    $("p").show() : shows all <p> elements

    $("p").css("color","red") : changes the color of all <p> elements to red

    $("p").css("color","red").hide() : changes the color of all <p> elements to red and hides them

    $("p").css("color","red").show() : changes the color of all <p> elements to red and shows them

    $("p").css("color","red").show().css("color","blue") : changes the color of all <p> elements to red, shows them and changes the color of all <p> elements to blue

    $(".test").hide() : hides all elements with class="test"

    $("#test").hide() : hides the element with id="test"

    jQuery selectors enable you to choose and control HTML components

    jQuery selectors are used to select HTML elements 

    CSS selectors are used to select HTML elements

    jQuery is customized to react to Events in an HTML page

    All the various guest activities that a site page ca react to are called Events

    jQuery Effects

    Display Effects:

    Hide()
    Show() 
    Toggle()

    Fading Effect:

    FadeIn()
    FadeOut()
    FadeToggle()
    FadeTo()

    Sliding Effect:

    SlideDown()
    SlideUp()
    SlideToggle(

    Other Effects:

    Animate()
    delay()
    stop()

    Events:

    Click()
    Hover()
    Focus()
    Blur()

    jQuery Methods:

    append()
    appendTo()
    before()
    after()
    remove()
    empty()
    clone()
    html()
    text()
    val()
    css()
    offset()
    position()
    scrollTop()
    scrollLeft()
    width()
    height()
    animate()
    delay()
    stop()

    jQuery Events:

    on()
    off()
    trigger()

    jQuery Callbacks:

    Callbacks are functions that are called when an event is triggered

    jQuery Callbacks are used to execute code after an event has been triggered

    show() and hide () methods ,you can use them to how or hide html elements

    toggle() can do both

    fadeIn(),fadeOut() to display or hide html element by gradually increasing or dicreasing their opacity 
    this methods only animates the opacity,it doesn't animate their dimensions.

    fadeToggle() can do both

    fadeTo() can be used to change the opacity of an element but you can only fade in the elements to a certain opacity level.

    slideUp() and slideDown() methods are utilized to hide or show the HTML elements by bit by bit diminishing or expanding their stature (for example by sliding them up or down).

    slideToggle() can be used to do both

    By vivifying their stature so that if the component is at first shown,it will be slide up.

    whenever covered up,it will be slide down

    for exaple, toggle between the slideUp() and slideDown() methods.

    animate() can be used to animate the HTML elements by changing their position or size.

    the animate() method is normally used to animate numeric CSS properties.

    for instance, width,stature,edge,cushioning,murkiness,top,left and so on.

    Yet the non-numeric properties,can't be animated utilizing the fundamental jQuery usefulness.

    for instance,visibility,display,opacity,background-color,background-image,background-position etc.

    stop() method is utilized to stop the jQuery animation or impacts as of now running on the chosen elements before it finishes.

    delay() method is used to delay the execution of the jQuery animation or impacts as of now running on the chosen elements before it finishes.

    jQuery Method Chaining

    It is a method that allows you to chain multiple jQuery methods.

    example:

    $("p").hide().show().css("color","red");

    $("p").hide().show().css("color","red").css("color","blue");

    $("p").hide().show().css("color","red").css("color","blue").show().css("color","red");

    $("p").hide().show().css("color","red").css("color","blue").show().css("color","red").show().css("color","blue");

    $("p").hide().show().css("color","red").css("color","blue").show().css("color","red").show().css("color","blue").show().css("color","red").show().css("color","blue");

    DOM Manipulation Methods

    DOM Manipulation Methods are used to manipulate the HTML elements

    The jQuery selector finds specific DOM elements and wraps them with jQuery objects

    for instance,

    document.getElementById() in the JS will return DOM object

    whereas $('#id') will return jQuery object. 

    after() strategically inserts content (new or existing DOM elements) after target elements which is specified by a selector.

    Syntax:

    $('selector expression').after('content');

    before() same as after() but before target elements which is specified by a selector.

    Syntax:

    $('selector expression').before('content');

    append() appends content (new or existing DOM elements) to target elements which is specified by a selector.

    Syntax:

    $('selector expression').append('content');

    prepend() same as append() but prepends content or inserts contect torward the start of an elements (new or existing DOM elements) to target elements which is specified by a selector.

    Syntax:

    $('selector expression').prepend('content');

    remove() removes target elements which is specified by a selector.

    Syntax:

    $('selector expression').remove();

    clone() clones target elements which is specified by a selector.

    Syntax:

    $('selector expression').clone();

    detach() removes target elements which is specified by a selector.

    Syntax:

    $('selector expression').detach();

    replaceWith() replaces target elements which is specified by a selector with content (new or existing DOM elements).

    Syntax:

    $('selector expression').replaceWith('content');

    replaceAll() same as replaceWith() but replaces all target elements which is specified by a selector with content (new or existing DOM elements).

    Syntax:

    $('selector expression').replaceAll('content');

    wrap() strategy wraps each target element with specified substance element.

    Syntax:

    $('selector expression').wrap('content');

    wrapAll() same as wrap() but wraps all target elements with specified substance element.

    Syntax:

    $('selector expression').wrapAll('content');

    wrapInner() same as wrap() but wraps each target element with specified substance element.

    Syntax:

    $('selector expression').wrapInner('content');

    wrapInnerAll() same as wrapInner() but wraps all target elements with specified substance element.

    Syntax:

    $('selector expression').wrapInnerAll('content');

    Attribute Manipulation:

    attr() is used to set or get the value of an attribute of the target elements which is specified by a selector.

    Syntax:

    $('selector expression').attr('attribute name','attribute value');

    removeAttr() is used to remove the value of an attribute of the target elements which is specified by a selector.

    Syntax:

    $('selector expression').removeAttr('attribute name');

    prop() is used to set or get the value of a property of the target elements which is specified by a selector.

    Syntax:

    $('selector expression').prop('property name','property value');

    removeProp() is used to remove the value of a property of the target elements which is specified by a selector.

    Syntax:

    $('selector expression').removeProp('property name');

    val() is used to set or get the value of an attribute of the target elements which is specified by a selector.

    Syntax:

    $('selector expression').val('value');

    removeVal() is used to remove the value of an attribute of the target elements which is specified by a selector.

    Syntax:

    $('selector expression').removeVal();

    Note:

    * The removeProp() and removeVal() methods are used to remove the property and value of the target elements which is specified by a selector.

    html() nethod gets or sets html  substance to the predefined DOM elements

    Syntax:

    $('selector expression').html('content');

    text() method gets or sets text substance to the predefined DOM elements

    Syntax:

    $('selector expression').text('content');

    Note:

    * The html() and text() methods are used to set or get the substance of the target elements which is specified by a selector.

    Dimension Manipulation:

    height() method gets or sets height of the target elements which is specified by a selector.

    Syntax:

    $('selector expression').height('content');

    width() method gets or sets width of the target elements which is specified by a selector.

    Syntax:

    $('selector expression').width('content');

    Note:

    * The height() and width() methods are used to set or get the height and width of the target elements which is specified by a selector.

    scrollTop() method gets or sets scrollTop of the target elements which is specified by a selector.

    Syntax:

    $('selector expression').scrollTop('content');

    scrollLeft() method gets or sets scrollLeft of the target elements which is specified by a selector.

    Syntax:

    $('selector expression').scrollLeft('content');

    Note:

    * The scrollTop() and scrollLeft() methods are used to set or get the scrollTop and scrollLeft of the target elements which is specified by a selector.

    $('selector expression').html('content');

    The above figure show various dimensions of an element

    offset() method gets or sets directions of the predetermined elements

    Syntax:

    $('selector expression').offset(options);

    Traversing Elements:

    each() method iterates over each predetermined component (indicated utilizing selector) and executes callback work for each component.

    Syntax:

    $('selector expression').each(function(index, element){

    });

    or

    $('selector expression').each(callback function);

    Note:

    * The each() method is used to iterate over each predetermined component (indicated utilizing selector) and executes callback work for each component.

    children() method to get the kid component of each component indicated utilizing selector articulation.

    Syntax:

    $('selector expression').children('selector expression');

    Note:

    * The children() method is used to get the kid component of each component indicated utilizing selector articulation.

    parent() method to get the parent component of each component indicated utilizing selector articulation.

    Syntax:

    $('selector expression').parent('selector expression');

    Note:

    * The parent() method is used to get the parent component of each component indicated utilizing selector articulation.

    siblings() method to get the sibling component of each component indicated utilizing selector articulation.

    Syntax:

    $('selector expression').siblings('selector expression');

    Note:

    * The siblings() method is used to get the sibling component of each component indicated utilizing selector articulation.

    find() method restores all the coordinating kid components of determined elements

    Syntax:

    $('selector expression').find('selector expression to find child elements');

    Note:

    * The find() method restores all the coordinating kid components of determined elements

    next() Method gets the quickly following kin of the predetermined component.

    Syntax:

    $('selector expression').next('selector expression');

    Note:

    * The next() Method gets the quickly following kin of the predetermined component.

    prev() Method gets the quickly previous kin of the predetermined component.

    Syntax:

    $('selector expression').prev('selector expression');

    Note:

    * The prev() Method gets the quickly previous kin of the predetermined component.

    CSS Manipulation:

    css() method gets or sets css property of the target elements which is specified by a selector.

    Syntax:

    $('selector expression').css('property','value');

    or 

    $('selector expression').css({'property':'value','property':'value'});

    or 

    $('selector expression').css({'property':'value','property':'value'},function(){

    });

    or 

    $('selector expression').css({
        'style property name':'value',
    });

    addClass() method includes single or various css class to the predefined elements.

    Syntax:

    $('selector expression').addClass('css class name');

    removeClass() method removes single or various css class from the predefined elements.

    Syntax:

    $('selector expression').removeClass('css class name');

    toggleClass() method toggles single or various css class from the predefined elements.

    Syntax:

    $('selector expression').toggleClass('css class name');

    jQuery Ajax(Asynchronous JavaScript And XML):

    JS includes features of sending asynchronous HTTP requests using XMLHttpRequest object.
    Ajax is about using this ability  of JS to send asynchronous HTTP requests and get the XML data as a response (also in other formats)
    and update the part of a page (using JS) without reloading or refreshing the entire web page.

    Advantages :

    * It is easy to use
    * It is fast
    * Cross-browser support
    * Simple methods to use
    * Ability to send GET and POST requests
    * Ability to Load json,xml,html or scripts

    ajax() method - it sends asynchronous HTTP requests to the server

    Syntax:

    $.ajax({

    });

    $.ajax(url);

    $.ajax(url,[options]);


    * The ajax() method sends asynchronous HTTP requests to the server

    * The ajax() method returns a jQuery object

    * The ajax() method can be used to send GET and POST requests


    $.ajax('/jQuery_Site/getdata','request url'
    {

    success: functionn (data,status,xhr){//success callback function

        $('p').append(data);
    
    }

});

sending Ajax request

examples:

// Create a new XMLHttpRequest object
var xhr = new XMLHttpRequest();

// Set the request method and URL
xhr.open('GET', 'https://example.com/data', true);

// Set the request headers
xhr.setRequestHeader('Content-Type', 'application/json');

// Send the request
xhr.send();

// Handle the response
xhr.onload = function() {
  if (xhr.status === 200) {
    var response = JSON.parse(xhr.responseText);
    console.log(response);
  } else {
    console.error('Error:', xhr.statusText);
  }
};


fetch('https://example.com/data')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));



$.ajax({
  type: 'GET',
  url: 'https://example.com/data',
  dataType: 'json',
  success: function(data) {
    console.log(data);
  },
  error: function(xhr, status, error) {
    console.error('Error:', error);
  }
});


Sending Http POST request using ajax()

$.ajax('/jquery/submitData',{

    type:'POST',// http method data:
    {myData: 'This is my data.'}, //data to submit
    success:function(data,status,xhr){
    $('p').append('status'+status+,'data:'+data);
},
error:function(jqxhr,textstatus,errorMessage){
    $('p').append('Error:'+errorMessage);
}

});

get() method ,technique sends offbeat HTTP GET solicitation to the server and recovers the information.

Syntax:

$.get(url,[data],[success],[dataType]);

or

$.get(url,[data],[success],[dataType],[error]);

or

$.get(url,[data],[success],[dataType],[error],[complete]);

or

$.get(url,[data],[callback]);

exaple:

$.get('https://example.com/data', function(data,textStatus,jqxhr) {//success callback

    alert('status: '+textStatus+',data:'+data);

});    


jQuery Events:

    * jQuery events are triggered by the user or the browser.

    * jQuery occasion strategies enable you to join occasion handler or fire local DOM occasions

  Event Handling:

    exaple:
    
    $('#saveBtn').click(function(){
    
    alert('save button clicked');

    });

    <input type="button" value="Save" id="saveBtn" />
    
  Event Objects:  Query passes an event obj to every event handler function.
    exaple:

    $('#saveBtn').click(function(eventObj){

        alert('X ='+eventObj.pageX+', Y ='+eventObj.pageY);

    });

    <input type="button" value="Save" id="saveBtn" />

    Hover Events: 

    methods:

    mouseenter() and mouseleave()

    mouseover()

    mouseout()

    mousemove()

    mousewheel()

    scroll()

    focus()

    blur()

    change()

    select()

    submit()

    keydown()

    keyup()

    keypress()

    contextmenu()

    load()

    unload()

    DOMContentLoaded()

    ready()

    on()

    off()

    trigger()

    triggerHandler()

    delegate()

    undelegate()

    mouseup()

    exaple:

    $('#myDiv').mouseenter(function(data)
    {
    
    $(this).css('background-color','green');
    
    });

    $('#myDiv').mouseleave(function(data)
    {
    
    $(this).css('background-color','red');
    
    });

    <div id="myDiv" style="width:100px; height:100px;"> </div>

    we can use hover() method

    exaple:

    $('#myDiv').hover(function()
    {$(this).css('background-color','green');},function()
    {$(this).css('background-color','red');});

    <div id="myDiv" style="width:100px; height:100px;"> </div>

  jQuery-UI:

    Interactions:

    *Interactions could be added by fundamental mouse-based practices to any component.

    * Interactions are used to create new behaviors in the UI.

    * Utilizing with interactions, We can make sortable records, resizeable components,drag and drop behaviours.

    1.Draggable: Enable drag capable usefulness on any DOM part.

    2.Droppable: Enable drop capable usefulness on any DOM part.

    3.Resizable: Enable resize capable usefulness on any DOM part.

    4.Sortable: Enable sort capable usefulness on any DOM part.

    5.Selectable: Enable select capable usefulness on any DOM part.

  Widgets:  

    *Widgets are used to create new behaviors in the UI.

    1.Accordion : Enable to collapse of the content, that is broken into logical sections.

    2.Button : Enable to create clickable buttons.

    3.Dialog : Enable to create modal dialogs.

    4.Menu : Enable to create menus.

    5.Progressbar : Enable to create progress bars.

    6.Tab : Enable to create tabs.

    7.Tooltip : Enable to create tooltips.

    8.Autocomplete : Enable to provides the suggestions while you type into the field.

    9.Datepicker : Enable to provides the date picker.

    10.Spinner : Enable to provides the spinner.

    11.Overlay : Enable to provides the overlay.

    12.Pagination : Enable to provides the pagination.

    13.Poll : Enable to provides the poll.

    14.Slider : Enable to provides the slider.

    15.Validator : Enable to provides the validation.

    16.Window : Enable to provides the window.

    17.Select menu : Enable a styleable select elements/elements.

    
    */