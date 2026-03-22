## 图表类型：大数据量柱图 (Large Scale Bar Chart)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
const dataCount = 5e5;
const data = generateData(dataCount);
option = {
  title: {
    text: echarts.format.addCommas(dataCount) + ' Data',
    left: 10
  },
  toolbox: {
    feature: {
      dataZoom: {
        yAxisIndex: false
      },
      saveAsImage: {
        pixelRatio: 2
      }
    }
  },
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'shadow'
    }
  },
  grid: {
    bottom: 90
  },
  dataZoom: [
    {
      type: 'inside'
    },
    {
      type: 'slider'
    }
  ],
  xAxis: {
    data: data.categoryData,
    silent: false,
    splitLine: {
      show: false
    },
    splitArea: {
      show: false
    }
  },
  yAxis: {
    splitArea: {
      show: false
    }
  },
  series: [
    {
      type: 'bar',
      data: data.valueData,
      // Set `large` for large data amount
      large: true
    }
  ]
};
function generateData(count) {
  let baseValue = Math.random() * 1000;
  let time = +new Date(2011, 0, 1);
  let smallBaseValue;
  function next(idx) {
    smallBaseValue =
      idx % 30 === 0
        ? Math.random() * 700
        : smallBaseValue + Math.random() * 500 - 250;
    baseValue += Math.random() * 20 - 10;
    return Math.max(0, Math.round(baseValue + smallBaseValue) + 3000);
  }
  const categoryData = [];
  const valueData = [];
  for (let i = 0; i < count; i++) {
    categoryData.push(
      echarts.format.formatTime('yyyy-MM-dd\nhh:mm:ss', time, false)
    );
    valueData.push(next(i).toFixed(2));
    time += 1000;
  }
  return {
    categoryData: categoryData,
    valueData: valueData
  };
}
```

