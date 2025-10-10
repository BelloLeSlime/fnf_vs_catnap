function onEvent(name, value1, value2)
	if name == "altblackout" then
		makeLuaSprite('image', value1, 0, -200);
		addLuaSprite('image', true);
		scaleObject('image', 3, 3);
		doTweenColor('hello', 'image', 'FFFFFFFF', 3, 'quartIn');
		setObjectCamera('image', 'game');
		runTimer('wait', value2);
	end
end

function onTimerCompleted(tag, loops, loopsleft)
	if tag == 'wait' then
		doTweenAlpha('byebye', 'image', 0, 0.3, 'linear');
	end
end

function onTweenCompleted(tag)
	if tag == 'byebye' then
		removeLuaSprite('image', true);
	end
end