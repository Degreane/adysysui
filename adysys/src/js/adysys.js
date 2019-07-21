$('.toolbox-element').draggable({
    proxy: 'clone'
})
$('#newHtmlPage').on('click', function (event) {
    event.preventDefault();
    console.log(event)
    alert('clicked')
    var randomId = Math.random() * 10000000

    var $newHtmlPage = $('<div id="html_' + randomId + '" class="easyui-droppable"></div>')

    $.ajax({
        url: 'build/html',
        data: {
            'newPage': 'html_' + randomId + '.html',
            'requested': 'AdySys Application '
        },
        method: 'POST',
    }).done(function (msg) {
        $('#HtmlPages').append($newHtmlPage)
        $newHtmlPage.window({
            width: 600,
            height: 320,
            closable: true,
            openAnimation: 'slide',
            closeAnimation: 'slide',
            minimizable: false,
            title: 'html_' + randomId,
            tools: [{
                iconCls: 'icon-add',
                handler: function () { alert('new') }
            }, {
                iconCls: 'icon-save',
                handler: function () { alert('save') }
            }]
        });
        var $newHtmlPageIFrame = $('<iframe class="easyui-droppable" id="iframe_' + randomId + '" src="/build/html/html_' + randomId + '.html" style="border:1px solid red;width:100%;height:100%"></iframe>')
        $newHtmlPage.append($newHtmlPageIFrame)
    }).fail(function (msg) {
        alert(msg['pageCreation'])
        console.log(msg)
    })

})
