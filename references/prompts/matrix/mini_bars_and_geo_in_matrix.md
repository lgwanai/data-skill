## 图表类型：矩阵坐标系下的微型条形图和地图 (Mini Bars and Geo in Matrix)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 外部数据结构分析
该图表需要特定的外部数据结构支撑。以下是下载后的数据结构示例，请将用户的真实数据映射为类似结构：

**数据文件 [/data/asset/geo/ch.geo.json]**:
```json
数据是一个对象 (Object)。包含的顶层字段示例：type, features。数据截取示例：
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              6.7881,
              46.405
            ],
            [
              6.7821,
              46.3785
            ],
            [
              6.7504,
              46.3455
            ],
            [
              6.8277,
              46.2695
            ],
            [
              6.7922,
         ...
```

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
var _colHeaders = ['Region and Time', 'Data A', 'Data B', 'Location'];
var _regionColIdx = 0;
var _geoColIdx = 3;
var _dataSourceList = [
  {
    name: '2021',
    data: [
      // 'Region', 'Data A', 'Data B'
      ['Valais', 1212, 2321],
      ['Ticino', 7181, 2114],
      ['Graubünden', 2763, 4212],
      ['Uri', 6122, 2942],
      ['Lucerne', 4221, 3411],
      ['Neuchâtel', 7221, 5121],
      ['Jura', 5121, 4121],
      ['Vaud', 6121, 3121],
      ['Thurgau', 7121, 2121],
      ['Schwyz', 8121, 1121]
    ]
  },
  {
    name: '2020',
    data: [
      // 'Region', 'Data A', 'Data B'
      ['Valais', 1010, 2221],
      ['Ticino', 7040, 1810],
      ['Graubünden', 2313, 4011],
      ['Uri', 6011, 2749],
      ['Lucerne', 3329, 3015],
      ['Neuchâtel', 7116, 4822],
      ['Jura', 4968, 3820],
      ['Vaud', 6027, 2928],
      ['Thurgau', 7011, 1725],
      ['Schwyz', 7311, 825]
    ]
  }
];
var _colorList = [ /* 请使用用户的真实数据数组替换此处 */ ];
function createChart() {
  option = {
    matrix: {
      x: {
        levelSize: 40,
        data: _colHeaders.map(function (item, colIdx) {
          return {
            value: item,
            size:
              colIdx === _geoColIdx
                ? '15%'
                : colIdx === _regionColIdx
                ? 120
                : undefined
          };
        }),
        itemStyle: { color: '#f0f8ff' },
        label: { fontWeight: 'bold' }
      },
      y: {
        data: _dataSourceList[0].data.map(function () {
          return '_'; // Any value is fine here, as we will not use it.
        }),
        show: false
      },
      body: {
        data: []
      },
      top: 25
    },
    legend: {},
    tooltip: {},
    grid: [],
    xAxis: [],
    yAxis: [],
    geo: [],
    series: []
  };
  // Assume every dataSourceList[i] has the same length; just for simplicity in this demo.
  var rowCount = _dataSourceList[0].data.length;
  for (var dataColIdx = 0; dataColIdx < _colHeaders.length; ++dataColIdx) {
    var dataExtentOnCol =
      dataColIdx === _regionColIdx || dataColIdx === _geoColIdx
        ? null
        : calculateDataExtentOnCol(_dataSourceList, dataColIdx);
    for (var dataRowIdx = 0; dataRowIdx < rowCount; ++dataRowIdx) {
      if (dataColIdx === _regionColIdx) {
        addCellPlainText(option, _dataSourceList, dataColIdx, dataRowIdx);
      } else if (dataColIdx === _geoColIdx) {
        addCellMiniGeo(option, _dataSourceList, dataColIdx, dataRowIdx);
      } else {
        addCellMiniBar(
          option,
          _dataSourceList,
          dataColIdx,
          dataRowIdx,
          dataExtentOnCol
        );
      }
    }
  }
  myChart.setOption(option);
}
function calculateDataExtentOnCol(dataSourceList, colIdx) {
  var min = Infinity;
  var max = -Infinity;
  dataSourceList.forEach((dataSource) => {
    dataSource.data.forEach((dataRow) => {
      var val = dataRow[colIdx];
      if (val < min) {
        min = val;
      }
      if (val > max) {
        max = val;
      }
    });
  });
  return [min, max];
}
function addCellPlainText(option, dataSourceList, dataColIdx, dataRowIdx) {
  // Assume every dataSourceList[i] has the same region names; just for simplicity in this demo.
  var dataSource = dataSourceList[0];
  option.matrix.body.data.push({
    value: dataSource.data[dataRowIdx][dataColIdx],
    coord: [dataColIdx, dataRowIdx]
  });
}
function addCellMiniBar(
  option,
  dataSourceList,
  dataColIdx,
  dataRowIdx,
  dataExtentOnCol
) {
  var id = 'mini-bar-' + dataColIdx + '-' + dataRowIdx;
  option.grid.push({
    id: id,
    coordinateSystem: 'matrix',
    coord: [dataColIdx, dataRowIdx],
    top: '15%',
    bottom: '15%'
  });
  option.xAxis.push({
    id: id,
    gridId: id,
    type: 'value',
    min: 0,
    max: dataExtentOnCol ? dataExtentOnCol[1] : undefined,
    scale: false,
    axisLine: { show: false },
    axisTick: { show: false },
    splitLine: { show: false },
    axisLabel: { show: false }
  });
  option.yAxis.push({
    id: id,
    gridId: id,
    type: 'category',
    boundaryGap: false,
    inverse: true,
    axisLine: { show: false },
    axisTick: { show: false },
    splitLine: { show: false },
    axisLabel: { show: false }
  });
  dataSourceList.forEach((dataSource, dataSourceIdx) => {
    option.series.push({
      type: 'bar',
      // `name` will be collected to legend.
      name: dataSource.name,
      xAxisId: id,
      yAxisId: id,
      label: { show: true, position: 'insideLeft' },
      barMinHeight: 2,
      barGap: '40%',
      barWidth: '40%',
      itemStyle: {
        color: _colorList[dataSourceIdx % _colorList.length]
      },
      encode: { label: 0 },
      // Make sure 2021 and 2020 have the same Y value (we use '' here) for better bar series layout.
      data: [[dataSource.data[dataRowIdx][dataColIdx], '']]
    });
  });
  return option;
}
function addCellMiniGeo(option, dataSourceList, dataColIdx, dataRowIdx) {
  var id = 'mini-geo-' + dataRowIdx;
  var regionName = dataSourceList[0].data[dataRowIdx][_regionColIdx];
  option.geo.push({
    id: id,
    map: 'target_map',
    animation: false,
    aspectScale: Math.cos((47 * Math.PI) / 180),
    coordinateSystem: 'matrix',
    coord: [dataColIdx, dataRowIdx],
    roam: false,
    selectedMode: false,
    tooltip: { show: false },
    regions: [
      {
        name: regionName,
        selected: true,
        select: {
          itemStyle: { color: '#0a41e6' }
        }
      }
    ],
    select: {
      label: { show: false }
    }
  });
}
function fetchGeoJSON() {
  myChart.showLoading();
  $.get(ROOT_PATH + '/data/asset/geo/ch.geo.json', function (geoJSON) {
    echarts.registerMap('target_map', geoJSON);
    createChart();
    myChart.hideLoading();
  });
}
fetchGeoJSON();
```

