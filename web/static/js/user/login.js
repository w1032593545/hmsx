;
var user_login_ops = {
    init:function(){
        this.eventBind()
    },
    eventBind:function(){
        $(".do-login").click(function(){
            var login_name = $("input[name=login_name]").val()
            var login_pwd = $("input[name=login_pwd]").val()
            console.log(login_name);
            console.log(login_pwd);
        })
        
                
    }
}
$(document).ready(function(){
    user_login_ops.init()
})