var page = require('webpage').create();
page.onConsoleMessage = function (msg) {
  console.log(msg);
}
page.open('https://www.baidu.com', function (status) {
  page.includeJs('http://ajax.googleapis.com/ajax/libs/jquery/1.6.1/jquery.min.js', function() {
    page.evaluate(function () {
      console.log($('title').text());
    });
    phantom.exit();
  });
});