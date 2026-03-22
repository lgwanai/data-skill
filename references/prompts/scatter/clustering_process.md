## 图表类型：聚合过程可视化 (Clustering Process)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
var originalData = [ /* 请使用用户的真实数据数组替换此处 */ ];
var DIM_CLUSTER_INDEX = 2;
var DATA_DIM_IDX = [0, 1];
var CENTER_DIM_IDX = [3, 4];
// See https://github.com/ecomfe/echarts-stat
var step = ecStat.clustering.hierarchicalKMeans(originalData, {
  clusterCount: 6,
  outputType: 'single',
  outputClusterIndexDimension: DIM_CLUSTER_INDEX,
  outputCentroidDimensions: CENTER_DIM_IDX,
  stepByStep: true
});
var colorAll = [ /* 请使用用户的真实数据数组替换此处 */ ];
var ANIMATION_DURATION_UPDATE = 1500;
function renderItemPoint(params, api) {
  var coord = api.coord([api.value(0), api.value(1)]);
  var clusterIdx = api.value(2);
  if (clusterIdx == null || isNaN(clusterIdx)) {
    clusterIdx = 0;
  }
  var isNewCluster = clusterIdx === api.value(3);
  var extra = {
    transition: []
  };
  var contentColor = colorAll[clusterIdx];
  return {
    type: 'circle',
    x: coord[0],
    y: coord[1],
    shape: {
      cx: 0,
      cy: 0,
      r: 10
    },
    extra: extra,
    style: {
      fill: contentColor,
      stroke: '#333',
      lineWidth: 1,
      shadowColor: contentColor,
      shadowBlur: isNewCluster ? 12 : 0,
      transition: ['shadowBlur', 'fill']
    }
  };
}
function renderBoundary(params, api) {
  var xVal = api.value(0);
  var yVal = api.value(1);
  var maxDist = api.value(2);
  var center = api.coord([xVal, yVal]);
  var size = api.size([maxDist, maxDist]);
  return {
    type: 'ellipse',
    shape: {
      cx: isNaN(center[0]) ? 0 : center[0],
      cy: isNaN(center[1]) ? 0 : center[1],
      rx: isNaN(size[0]) ? 0 : size[0] + 15,
      ry: isNaN(size[1]) ? 0 : size[1] + 15
    },
    extra: {
      renderProgress: ++targetRenderProgress,
      enterFrom: {
        renderProgress: 0
      },
      transition: 'renderProgress'
    },
    style: {
      fill: null,
      stroke: 'rgba(0,0,0,0.2)',
      lineDash: [4, 4],
      lineWidth: 4
    }
  };
}
function makeStepOption(option, data, centroids) {
  var newCluIdx = centroids ? centroids.length - 1 : -1;
  var maxDist = 0;
  for (var i = 0; i < data.length; i++) {
    var line = data[i];
    if (line[DIM_CLUSTER_INDEX] === newCluIdx) {
      var dist0 = Math.pow(line[DATA_DIM_IDX[0]] - line[CENTER_DIM_IDX[0]], 2);
      var dist1 = Math.pow(line[DATA_DIM_IDX[1]] - line[CENTER_DIM_IDX[1]], 2);
      maxDist = Math.max(maxDist, dist0 + dist1);
    }
  }
  var boundaryData = centroids
    ? [[centroids[newCluIdx][0], centroids[newCluIdx][1], Math.sqrt(maxDist)]]
    : [];
  option.options.push({
    series: [
      {
        type: 'custom',
        encode: {
          tooltip: [0, 1]
        },
        renderItem: renderItemPoint,
        data: data
      },
      {
        type: 'custom',
        renderItem: renderBoundary,
        animationDuration: 3000,
        silent: true,
        data: boundaryData
      }
    ]
  });
}
var targetRenderProgress = 0;
option = {
  timeline: {
    top: 'center',
    right: 50,
    height: 300,
    width: 10,
    inverse: true,
    autoPlay: false,
    playInterval: 2500,
    symbol: 'none',
    orient: 'vertical',
    axisType: 'category',
    label: {
      formatter: 'step {value}',
      position: 10
    },
    checkpointStyle: {
      animationDuration: ANIMATION_DURATION_UPDATE
    },
    data: []
  },
  baseOption: {
    animationDurationUpdate: ANIMATION_DURATION_UPDATE,
    transition: ['shape'],
    tooltip: {},
    xAxis: {
      type: 'value'
    },
    yAxis: {
      type: 'value'
    },
    series: [
      {
        type: 'scatter'
      }
    ]
  },
  options: []
};
makeStepOption(option, originalData);
option.timeline.data.push('0');
for (var i = 1, stepResult; !(stepResult = step.next()).isEnd; i++) {
  makeStepOption(
    option,
    echarts.util.clone(stepResult.data),
    echarts.util.clone(stepResult.centroids)
  );
  option.timeline.data.push(i + '');
}
```

