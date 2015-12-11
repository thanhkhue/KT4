
var imgSrcs = ["static/blog/images/khue.png", "static/blog/images/slider2.png"];

setInterval(function() {
    $("body").css("background", "url(" + imgSrcs[imgSrcs.push(imgSrcs.shift())-1] + ")");
}, 3500);


// $(document).ready(function(){
//     $("#toggle").on("click", function(){
//         $("div").toggle(5000);
//     });
//     $("#interval").on("click", function(){
//         jQuery.fx.interval = 500;
//     });
// });
