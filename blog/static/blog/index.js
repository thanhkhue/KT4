
var imgSrcs = ["static/blog/images/1.png", "static/blog/images/2.png"];

setInterval(function() {
    $("body").css("background", "url(" + imgSrcs[imgSrcs.push(imgSrcs.shift())-1] + ")");
}, 3000);


// $(document).ready(function(){
//     $("#toggle").on("click", function(){
//         $("div").toggle(5000);
//     });
//     $("#interval").on("click", function(){
//         jQuery.fx.interval = 500;
//     });
// });
