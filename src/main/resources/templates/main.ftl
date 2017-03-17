<!DOCTYPE html>
<html lang="en" ng-app="predict">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="../bootstrap-3.3.7-dist/css/bootstrap.css" type="text/css" rel="stylesheet"/>
    <link href="../bootstrap-3.3.7-dist/css/processbar.css" type="text/css" rel="stylesheet"/>
    <script src="../js/angular.min.js"></script>
    <script src="../js/predict.js"></script>
</head>
<body>

<nav class="navbar navbar-inverse navbar-static-top" role="navigation">
    <div class="navbar-inner">
        <div class="container-fluid col-md-offset-5">
            <ul class="nav navbar-nav">
                <li><a class="navbar-brand" href="#">北京地区店铺预测系统</a></li>
                <li><a><input type="text" class="nav navbar-nav btn-xs" placeholder="search"/></li></a>
                <li><a><button class="btn btn-xs">查询</button></a></li>
            </ul>
        </div>
    </div>

</nav>

<div class="container-fluid" ng-controller="predictController">
    <div class="col-lg-8 col-md-offset-1">
        <div class="panel panel-primary">
            <div class="panel-heading">
                <h3 class="panel-title">查询</h3>
            </div>
            <div class="panel-body">
                <form class="form-horizontal">
                    <div class="form-group">
                        <label for="inputEmail3" class="col-sm-2 control-label">纬度</label>
                        <div class="col-sm-8">
                            <input type="number" class="form-control" id="inputEmail3" placeholder="lon" ng-model="lon">
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="inputPassword3" class="col-sm-2 control-label">经度</label>
                        <div class="col-sm-8">
                            <input type="number" class="form-control" id="inputPassword3" placeholder="lat"
                                   ng-model="lat">
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="inputPassword3" class="col-sm-2 control-label">均价</label>
                        <div class="col-sm-8">
                            <input type="number" class="form-control" id="inputPassword3" placeholder="avgPrice"
                                   ng-model="avgPrice">
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
        <div class="panel panel-primary">
            <div class="panel-heading">
                <h3 class="panel-title">查询结果</h3>
            </div>
            <div class="panel-body">
                <div class="col-lg-8">
                    <div style="margin-top: 20px;margin-left: -15px"><label>查询结果百分比</label>
                        <div/>
                        <div class="progress">
                            <div class="progress-bar progress-bar-info progress-bar-striped active"
                                 style="width: 85%;">
                                <div class="progress-value">85%</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>


</body>
</html>