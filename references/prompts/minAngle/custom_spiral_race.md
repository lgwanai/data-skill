## 图表类型：自定义螺旋线竞速 (Custom Spiral Race)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
var _animationDuration = 5000;
var _animationDurationUpdate = 7000;
var _animationEasingUpdate = 'linear';
// prettier-ignore
var _radianLabels = [ /* 请使用用户的真实数据数组替换此处 */ ];
var _valOnRoundRadian = _radianLabels.length;
var _radianStep = Math.PI / 45;
var _barWidthValue = 0.4;
var _valOnRadiusStep = 4;
// angleAxis.startAngle is 90 by default.
var _startRadian = Math.PI / 2;
// prettier-ignore
var _colors = [
    { fill: '#5470c6', text: '#2747a5' },
    { fill: '#91cc75', text: '#447f27' },
    { fill: '#fac858', text: '#a0761c' }
];
var _currentDataIndex = 0;
// prettier-ignore
var _datasourceList = [
    [[1, 3], [2, 6], [3, 9]],
    [[1, 12], [2, 16], [3, 14]],
    [[1, 17], [2, 22], [3, 19]],
    [[1, 19], [2, 33], [3, 24]],
    [[1, 24], [2, 42], [3, 29]],
    [[1, 27], [2, 47], [3, 41]],
    [[1, 36], [2, 52], [3, 52]],
    [[1, 46], [2, 59], [3, 63]],
    [[1, 60], [2, 63], [3, 69]],
];
var _barNamesByOrdinal = { 1: 'A', 2: 'B', 3: 'C' };
function getMaxRadius() {
  var radius = 0;
  var datasource = _datasourceList[_currentDataIndex];
  for (var j = 0; j < datasource.length; j++) {
    var dataItem = datasource[j];
    radius = Math.max(radius, getSpiralValueOnRadius(dataItem[0], dataItem[1]));
  }
  return Math.ceil(radius * 1.2);
}
function getSpiralValueOnRadius(valOnStartRadius, valOnEndAngle) {
  return (
    valOnStartRadius + _valOnRadiusStep * (valOnEndAngle / _valOnRoundRadian)
  );
}
function getSpiralRadius(startRadius, endRadian, radiusStep) {
  return (
    startRadius + radiusStep * ((_startRadian - endRadian) / (Math.PI * 2))
  );
}
function renderItem(params, api) {
  var children = [];
  var dataIdx = params.dataIndex;
  addShapes(
    params,
    api,
    children,
    api.value(0),
    api.value(1),
    _colors[dataIdx]
  );
  return {
    type: 'group',
    children: children
  };
}
function addShapes(
  params,
  api,
  children,
  valOnStartRadius,
  valOnEndRadian,
  color
) {
  var coords = api.coord([valOnStartRadius, valOnEndRadian]);
  var startRadius = coords[2];
  var endRadian = coords[3];
  var widthRadius = api.coord([_barWidthValue, 0])[2];
  addPolygon(params, children, widthRadius, startRadius, endRadian, color);
  addLabel(params, children, widthRadius, startRadius, endRadian, color);
}
function addPolygon(
  params,
  children,
  widthRadius,
  startRadius,
  endRadian,
  color
) {
  children.push({
    type: 'polygon',
    shape: {
      points: makeShapePoints(params, widthRadius, startRadius, endRadian)
    },
    extra: {
      widthRadius: widthRadius,
      startRadius: startRadius,
      endRadian: endRadian,
      transition: ['widthRadius', 'startRadius', 'endRadian']
    },
    style: {
      fill: color.fill
    },
    during: function (apiDuring) {
      apiDuring.setShape(
        'points',
        makeShapePoints(
          params,
          apiDuring.getExtra('widthRadius'),
          apiDuring.getExtra('startRadius'),
          apiDuring.getExtra('endRadian')
        )
      );
    }
  });
}
function makeShapePoints(params, widthRadius, startRadius, endRadian) {
  var points = [];
  var radiusStep = getRadiusStepByWidth(widthRadius);
  // angleAxis.clockwise is true by default. So when rotate clickwisely, radian decreases.
  for (
    var iRadian = _startRadian, end = endRadian - _radianStep;
    iRadian > end;
    iRadian -= _radianStep
  ) {
    iRadian < endRadian && (iRadian = endRadian);
    var iRadius = getSpiralRadius(
      startRadius - widthRadius,
      iRadian,
      radiusStep
    );
    points.push(convertToPolarPoint(params, iRadius, iRadian));
  }
  for (
    var iRadian = endRadian;
    iRadian < _startRadian + _radianStep;
    iRadian += _radianStep
  ) {
    iRadian > _startRadian && (iRadian = _startRadian);
    var iRadius = getSpiralRadius(
      startRadius + widthRadius,
      iRadian,
      radiusStep
    );
    points.push(convertToPolarPoint(params, iRadius, iRadian));
  }
  return points;
}
function getRadiusStepByWidth(widthRadius) {
  return (widthRadius / _barWidthValue) * _valOnRadiusStep;
}
function addLabel(
  params,
  children,
  widthRadius,
  startRadius,
  endRadian,
  color
) {
  var point = makeLabelPosition(params, widthRadius, startRadius, endRadian);
  children.push({
    type: 'text',
    x: point[0],
    y: point[1],
    transition: [],
    extra: {
      startRadius: startRadius,
      endRadian: endRadian,
      widthRadius: widthRadius,
      transition: ['startRadius', 'endRadian', 'widthRadius']
    },
    style: {
      text: makeText(endRadian),
      fill: color.text,
      stroke: '#fff',
      lineWidth: 3,
      fontSize: 16,
      align: 'center',
      verticalAlign: 'middle',
      rich: {
        round: { fontSize: 24 },
        percent: { fontSize: 18 }
      }
    },
    z2: 50,
    during: function (apiDuring) {
      var endRadian = apiDuring.getExtra('endRadian');
      var point = makeLabelPosition(
        params,
        apiDuring.getExtra('widthRadius'),
        apiDuring.getExtra('startRadius'),
        endRadian
      );
      apiDuring.setTransform('x', point[0]).setTransform('y', point[1]);
      apiDuring.setStyle('text', makeText(endRadian));
    }
  });
  function makeText(endRadian) {
    var radian = _startRadian - endRadian;
    var PI2 = Math.PI * 2;
    var round = Math.floor(radian / PI2);
    var percent = (((radian / PI2) % 1) * 100).toFixed(1) + '%';
    return 'Round {round|' + round + '}\n{percent|' + percent + '}';
  }
}
function makeLabelPosition(params, widthRadius, startRadius, endRadian) {
  var radiusStep = getRadiusStepByWidth(widthRadius);
  var iRadius = getSpiralRadius(startRadius, endRadian, radiusStep);
  return convertToPolarPoint(params, iRadius, endRadian - 10 / iRadius);
}
function convertToPolarPoint(renderItemParams, radius, radian) {
  return [
    Math.cos(radian) * radius + renderItemParams.coordSys.cx,
    -Math.sin(radian) * radius + renderItemParams.coordSys.cy
  ];
}
option = {
  animationDuration: _animationDuration,
  animationDurationUpdate: _animationDurationUpdate,
  animationEasingUpdate: _animationEasingUpdate,
  dataset: {
    source: _datasourceList[_currentDataIndex]
  },
  tooltip: {},
  angleAxis: {
    type: 'value',
    splitArea: { show: true },
    axisLabel: {
      formatter: function (val) {
        return _radianLabels[val];
      },
      color: 'rgba(0,0,0,0.2)'
    },
    axisLine: { lineStyle: { color: 'rgba(0,0,0,0.2)' } },
    min: 0,
    max: _valOnRoundRadian
  },
  radiusAxis: {
    type: 'value',
    interval: 1,
    splitLine: { show: false },
    axisLabel: {
      color: 'rgba(0,0,0,0.6)',
      formatter: function (value) {
        return _barNamesByOrdinal[value] || '';
      }
    },
    axisTick: { show: false },
    axisLine: { lineStyle: { color: 'rgba(0,0,0,0.2)' } },
    min: 0,
    max: getMaxRadius()
  },
  polar: {},
  series: [
    {
      type: 'custom',
      coordinateSystem: 'polar',
      renderItem: renderItem
    }
  ]
};
function next() {
  ++_currentDataIndex;
  myChart.setOption({
    dataset: {
      source: _datasourceList[_currentDataIndex]
    },
    radiusAxis: {
      max: getMaxRadius()
    }
  });
  if (_currentDataIndex < _datasourceList.length - 1) {
    setTimeout(next, _animationDurationUpdate);
  }
}
setTimeout(next, 1000);
```

