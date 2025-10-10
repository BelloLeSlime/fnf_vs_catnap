function onUpdate(elapsed)


	local lol = math.random(1,2)

	if (lol >= 1) then
	
		doTweenAngle('theo', 'iconP2', -3, stepCrochet*0.00000000009, 'circOut')
	end

	if (lol >= 2) then

		doTweenAngle('theo', 'iconP2', 3, stepCrochet*0.00000000009, 'circOut')
	end
end