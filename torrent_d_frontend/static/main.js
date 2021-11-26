// var WebTorrent = require('webtorrent')

requirejs(["webtorrent.min"], function(util) {
    //This function is called when scripts/helper/util.js is loaded.
    //If util.js calls define(), then this function is not fired until
    //util's dependencies have loaded, and the util argument will hold
    //the module value for "helper/util".

    console.log("helllo world")
    var client = new util()
    // console.log(client)
    //deadpool2
    // var magnetURI="magnet:?xt=urn:btih:00102086b401f8ce049be55410ff9c69d87bb740&dn=Deadpool%202%20(2018)%20%5bWEBRip%5d%20%5b720p%5d%20%5bYTS.AM%5d&tr=udp%3a%2f%2ftracker.coppersurfer.tk%3a6969%2fannounce&tr=udp%3a%2f%2f9.rarbg.com%3a2710%2fannounce&tr=udp%3a%2f%2fp4p.arenabg.com%3a1337&tr=udp%3a%2f%2ftracker.leechers-paradise.org%3a6969&tr=udp%3a%2f%2ftracker.internetwarriors.net%3a1337&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce"


    var torrentId = 'magnet:?xt=urn:btih:08ada5a7a6183aae1e09d831df6748d566095a10&dn=Sintel&tr=udp%3A%2F%2Fexplodie.org%3A6969&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Ftracker.empire-js.us%3A1337&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=wss%3A%2F%2Ftracker.btorrent.xyz&tr=wss%3A%2F%2Ftracker.fastcast.nz&tr=wss%3A%2F%2Ftracker.openwebtorrent.com&ws=https%3A%2F%2Fwebtorrent.io%2Ftorrents%2F&xs=https%3A%2F%2Fwebtorrent.io%2Ftorrents%2Fsintel.torrent'

    client.add(torrentId, { path: '/home/adil/adilt' }, function (torrent) {
        console.log("downloading....")
        torrent.on('done', function () {
          console.log('torrent download finished')
        })
    })
    // client.add(torrentId, function (torrent) {
    //     // Torrents can contain many files. Let's use the .mp4 file
    //     var file = torrent.files.find(function (file) {
    //       return file.name.endsWith('.mp4')
    //     })
    //     console.log(file)
    //     // Display the file by adding it to the DOM.
    //     // Supports video, audio, image files, and more!
    //     file.appendTo('body')
    //   })
});

// var client = new WebTorrent()