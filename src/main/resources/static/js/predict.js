var predictModule = angular.module('predict', []);
predictModule.controller("predictController", function ($scope,$http) {
    $scope.submit = function () {
        $http({
            method: "GET",
            url: "/rest/predict/",
            params: {
                'lon': $scope.lon,
                'lat': $scope.lat,
                'avgPrice':$scope.avgPrice
            }
        }).then(function (response) {
                $scope.data=response.data
                console.log( $scope.data)
        }).catch(function (response) {
           //todo
        });
    }
});

