$(document).ready(function() {

    namespace = '/test';

    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);

    socket.on('resp', function(msg){
        var contacts = '';
        var get_contact = msg.contacts
        for (i = 0; i < get_contact.length; i++) {
                var value = get_contact[i];
                if (typeof value === "undefined") {
                    console.log("Gay");
                }
                else {
                    contacts = contacts + value + '\n';
                };
          };

//        console.log(contacts);
        $('#contacts').html(contacts);

    });

});


$(document).ready(function(){

    namespace = '/ping';

    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);

    var ping_pong_times = [];
            var start_time;
            window.setInterval(function() {
                start_time = (new Date).getTime();
                socket.emit('my_ping');
            }, 1000);

    socket.on('my_pong', function() {
                var latency = (new Date).getTime() - start_time;
                ping_pong_times.push(latency);
                ping_pong_times = ping_pong_times.slice(-30); // keep last 30 samples
                var sum = 0;
                for (var i = 0; i < ping_pong_times.length; i++)
                    sum += ping_pong_times[i];
                $('#ping-pong').text(Math.round(10 * sum / ping_pong_times.length) / 10);
            });

}

)

$(document).ready(function() {

    namespace = '/os';

    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);

    socket.on('resp', function(msg){
     $('#os').html(msg.os);


    });

});