;
var account_index_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){
        var that = this;
        $(".wrap_search .search").click(function(){
            $(".wrap_search").submit();  /*搜索，传递参数mix_kw混合查询关键字*/
        });

        $(".remove").click( function(){
            that.ops( "remove",$(this).attr("data") );
        } );

        $(".recover").click( function(){
            that.ops( "recover",$(this).attr("data") );
        } );
    },
    ops:function( act,id ){
        var callback = {
            'ok':function(){
                $.ajax({
                    url:common_ops.buildUrl( "/account/ops" ),
                    type:'POST',
                    data:{
                        act:act,
                        id:id
                    },
                    dataType:'json',
                    success:function( res ){
                        var callback = null;
                        if( res.code == 200 ){
                            callback = function(){
                                window.location.href = window.location.href;
                            }
                        }
                        common_ops.alert( res.msg,callback );
                    }
                });
            },
            'cancel':null
        };
        /*同意进行删除前，进行一个提示，否则删除很危险，在common.js中定义了callback方法*/
        common_ops.confirm( ( act == "remove" ? "确定删除？":"确定恢复？" ), callback );
    }
};
$(document).ready( function(){
    account_index_ops.init();
} );
