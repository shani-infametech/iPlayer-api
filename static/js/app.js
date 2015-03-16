angular.module('ui.bootstrap', []);

var app = angular.module('bbc-movies', ['ui.bootstrap']);

app.controller('MoviesController', function ($scope, $http) {
    $scope.start = 0;
    $scope.count = 5;
    $scope.movies = [];
    $scope.addMore = function () {
        $scope.loading = true;
        $http.get('/movies/get/' + $scope.start + '/' + $scope.count + '/160/90')
        .success(function (data, status, headers, config) {
            for (key in data) {
                $scope.movies.push(data[key]);
            }
            $scope.hasMore = data.length > 0;
            $scope.start += $scope.count;
            $scope.loading = false;
        })
        .error(function (data, status, headers, config) {
            console.log(data);
            $scope.loading = false;
        });
    }
    $scope.addMore();
});