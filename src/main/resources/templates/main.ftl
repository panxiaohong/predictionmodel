<!DOCTYPE html>
<html lang="en" ng-app="predict">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="../bootstrap-3.3.7-dist/css/bootstrap.css" type="text/css" rel="stylesheet"/>
    <script src="../js/angular.min.js"></script>
    <script src="../js/predict.js"></script>
</head>
<body>

<nav class="navbar navbar-inverse" role="navigation">
    <div class="container-fluid">
        <div class="navbar-header">
            <a class="navbar-brand" href="#">北京地区店铺预测系统</a>
        </div>
    </div>
</nav>


<div class="container-fluid" ng-controller="predictController">
    <div class="col-lg-3 col-md-offset-1">
        <div class="panel panel-primary">
            <div class="panel-heading">
                <h3 class="panel-title">查询</h3>
            </div>
            <div class="panel-body">
                <form class="form-horizontal">
                    <div class="form-group">
                        <label for="inputEmail3" class="col-sm-2 control-label" >纬度</label>
                        <div class="col-sm-8">
                            <input type="number" class="form-control" id="inputEmail3" placeholder="lon" ng-model="lon">
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="inputPassword3" class="col-sm-2 control-label" >经度</label>
                        <div class="col-sm-8">
                            <input type="number" class="form-control" id="inputPassword3" placeholder="lat" ng-model="lat">
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="inputPassword3" class="col-sm-2 control-label">均价</label>
                        <div class="col-sm-8">
                            <input type="number" class="form-control" id="inputPassword3" placeholder="avgPrice" ng-model="avgPrice">
                        </div>
                    </div>
                    <div class="form-group">
                        <div class="col-sm-offset-8 col-sm-10">
                            <button type="submit" class="btn btn-primary" ng-click="submit()">查询</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
    <div class="col-lg-3">

        <div class="panel panel-primary">
            <div class="panel-heading">
                <h3 class="panel-title">查询结果</h3>
            </div>
            <div class="panel-body" >
                <p>在您输入的添加下预测的结果为</p>
                <p>{{data.hello}}</p>
            </div>
        </div>

    </div>
</div>










</body>
</html>