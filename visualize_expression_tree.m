function visualize_expression_tree()
    % 读取 JSON 文件
    filename = 'expression_tree.json';
    jsonText = fileread(filename);
    treeData = jsondecode(jsonText);

    % 创建一个新的图形窗口
    figure;

    % 初始化绘图
    hold on;
    axis off;

    % 绘制表达式树
    drawTree(treeData, 0.5, 1, 0.25);

    % 设置图形样式
    title('Expression Tree');
    hold off;
end

function drawTree(node, x, y, dx)
    if isempty(node)
        return;
    end
    
    % 绘制当前节点
    plot(x, y, 'o', 'MarkerSize', 10, 'MarkerFaceColor', 'b');
    text(x, y, node.value, 'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'right');
    
    % 计算子节点位置
    if ~isempty(node.left)
        line([x, x-dx], [y, y-0.2], 'Color', 'k');
        drawTree(node.left, x-dx, y-0.2, dx/2);
    end
    if ~isempty(node.right)
        line([x, x+dx], [y, y-0.2], 'Color', 'k');
        drawTree(node.right, x+dx, y-0.2, dx/2);
    end
    if isfield(node, 'parameters') && ~isempty(node.parameters)
        for i = 1:length(node.parameters)
            line([x, x], [y, y-0.2*(i+1)], 'Color', 'k', 'LineStyle', '--');
            drawTree(node.parameters{i}, x, y-0.2*(i+1), dx/2);
        end
    end
end
