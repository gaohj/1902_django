var gulp = require('gulp');
var cssnano = require("gulp-cssnano")
var rename = require("gulp-rename")
var uglify = require("gulp-uglify")
var concat = require("gulp-concat")
var imagemin = require("gulp-imagemin")
var cache = require("gulp-cache")
var bs = require("browser-sync").create()
var sass = require("gulp-sass")
var util = require("gulp-util")
var sourcemaps = require("gulp-sourcemaps")
gulp.task("hello",done=> {
    console.log("hello world");
    done();
});
//上面是4版本的

var path = {
    'html':'./templates/**/',
    'css':'./src/css/**/',
    'js':'./src/js/**/',
    'images':'./src/images/',
    'css_dist':'./dist/css/',
    'js_dist':'./dist/js/',
    'images_dist':'./dist/images/',
}

var gulp = require('gulp');
gulp.task("greet",function(){
    console.log("hello world");
});
//上面是 3版本的


gulp.task("scss",function(){
    gulp.src(path.css,+"*.scss")
        .pipe(sourcemaps.init())
        .pipe(sass().on("error",sass.logError))
        .pipe(cssnano())
        .pipe(rename({"suffix":".min"}))
        .pipe(sourcemaps.write())
        .pipe(gulp.dest(path.css_dist))
        .pipe(bs.stream())

})

gulp.task("html",function() {
    gulp.src(path.html +"*.html")
    .pipe(bs.stream())
})

gulp.task("concatjs",function(){
    gulp.src("./src/js/*.js")
    .pipe(sourcemaps.init())
    .pipe(uglify().on("error",sass.logError))
    .pipe(rename({"suffix":".min"}))
    .pipe(sourcemaps.write())
    .pipe(gulp.dest("./dist/js/"))
    .pipe(bs.stream())
})

gulp.task("images",function(){
    gulp.src("./src/images/*.*")
    .pipe(cache(imagemin()))
    .pipe(gulp.dest(path.images_dist))
    .pipe(bs.stream())
})

//定义一个监听的任务
gulp.task("watchs",function(){
    gulp.watch(path.css + ".scss",['scss']),
    gulp.watch(path.html + ".html",['html']),
    gulp.watch(path.images + "*.*",['images']),
    gulp.watch(path.js + ".js",['concatjs'])
})

gulp.task("bs",function(){
    bs.init({
        'server':{
            'baseDir':'./'
        }
    })
})


gulp.task("default",['bs','watchs'])

