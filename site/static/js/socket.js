$(document).ready(function () {

    namespace = '/get';

    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);

    socket.on('resp', function (msg) {
        console.log('hehe')
        console.log(msg)
        var social = '';
        var get_contact = msg.social
        for (i = 0; i < get_contact.length; i++) {
            var value = get_contact[i];
            if (typeof value === "undefined") {
                console.log("Gay");
            }
            else {
                social = social + value + '\n';
            };
        };

        console.log(social);
        $('#social').html(social);

    });

});