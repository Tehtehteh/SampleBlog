$(document).ready(function(){
    getBlogPosts();
});
function getBlogPosts(){
    $.ajax({
        type: 'GET',
        url : '/api/blogposts',
        success:function(posts){
            $('.fa').removeClass('hidden');
            for(let i = 0; i < posts.length; i++){
                var str = `
                <div class="panel panel-default">
                <div class="panel-heading">
                    <div class="text-center">
                        <div class="row">
                            <div class="col-sm-9">
                                <h4 class="pull-left">{0}</h4>
                            </div>
                            <div class="col-sm-3">
                                <p class="pull-right small" style="margin-bottom: 10px;">{1}</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="panel-body">
                    <div class="row">
                        <div class="col-md-12">
                            <div class="col-md-4">
                                <img class="img-thumbnail" width="300" height="400" src="{2}"/>
                            </div>
                            <div class="col-md-8">
                                <p>{3}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>`;
            str = str.format(posts[i].title, new Date(posts[i].date), posts[i].pic, posts[i].text);
            $('.body-container').append(str);
            }
            $('.body-container').fadeIn(2000);
            $('.fa').toggleClass('hidden');
        },
    })
};
$('li[role=presentation]:first').toggleClass('active');
$('li[role=presentation]').click(function(){
$('li.active').removeClass('active');
 $(this).toggleClass('active');
})
 /* "{0}{1}".format(20,16) -> "2016" */
String.prototype.format = function() {
    var formatted = this;
    for( var arg in arguments ) {
        formatted = formatted.replace("{" + arg + "}", arguments[arg]);
    }
    return formatted;
};