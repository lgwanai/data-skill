## 图表类型：凹凸图 (Bump Chart (Ranking))

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
const names = [ /* 请使用用户的真实数据数组替换此处 */ ];
const years = [ /* 请使用用户的真实数据数组替换此处 */ ];
const shuffle = (array) => {
  let currentIndex = array.length;
  let randomIndex = 0;
  while (currentIndex > 0) {
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;
    [array[currentIndex], array[randomIndex]] = [
      array[randomIndex],
      array[currentIndex]
    ];
  }
  return array;
};
const generateRankingData = () => {
  const map = new Map();
  const defaultRanking = Array.from({ length: names.length }, (_, i) => i + 1);
  for (const _ of years) {
    const shuffleArray = shuffle(defaultRanking);
    names.forEach((name, i) => {
      map.set(name, (map.get(name) || []).concat(shuffleArray[i]));
    });
  }
  return map;
};
const generateSeriesList = () => {
  const seriesList = [];
  const rankingMap = generateRankingData();
  rankingMap.forEach((data, name) => {
    const series = {
      name,
      symbolSize: 20,
      type: 'line',
      smooth: true,
      emphasis: {
        focus: 'series'
      },
      endLabel: {
        show: true,
        formatter: '{a}',
        distance: 20
      },
      lineStyle: {
        width: 4
      },
      data
    };
    seriesList.push(series);
  });
  return seriesList;
};
option = {
  title: {
    text: 'Bump Chart (Ranking)'
  },
  tooltip: {
    trigger: 'item'
  },
  grid: {
    left: 30,
    right: 110,
    bottom: 30,
    containLabel: true
  },
  toolbox: {
    feature: {
      saveAsImage: {}
    }
  },
  xAxis: {
    type: 'category',
    splitLine: {
      show: true
    },
    axisLabel: {
      margin: 30,
      fontSize: 16
    },
    boundaryGap: false,
    data: years
  },
  yAxis: {
    type: 'value',
    axisLabel: {
      margin: 30,
      fontSize: 16,
      formatter: '#{value}'
    },
    inverse: true,
    interval: 1,
    min: 1,
    max: names.length
  },
  series: generateSeriesList()
};
```

