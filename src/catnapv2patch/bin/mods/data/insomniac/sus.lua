--easy script configs
IntroTextSize = 35 --Size of the text for the Now Playing thing.
IntroSubTextSize = 40 --size of the text for the Song Name.
IntroTagColor = '0'	--Color of the tag at the end of the box.
IntroTagWidth = 130	--Width of the box's tag thingy.
--easy script configs

--actual script
function onCreate()
	--the tag at the end of the box
	makeLuaSprite('JukeBoxTag', 'empty', -305-IntroTagWidth, 15)
	makeGraphic('JukeBoxTag', 220+IntroTagWidth, 100, IntroTagColor)
	setObjectCamera('JukeBoxTag', 'hud')
	addLuaSprite('JukeBoxTag', true)

	--the box
	makeLuaSprite('JukeBox', 'empty', -305-IntroTagWidth, 15)
	makeGraphic('JukeBox', 190, 100, '0')
	setObjectCamera('JukeBox', 'hud')
	addLuaSprite('JukeBox', true)
	
	--the text for the "song name" bit
	makeLuaText('JukeBoxText', '@bucketofshrimp', 330, -305-IntroTagWidth, 180)
	setTextAlignment('JukeBoxText', 'left')
	setObjectCamera('JukeBoxText', 'game')
	setTextSize('JukeBoxText', IntroTextSize)
	addLuaText('JukeBoxText')
	setProperty('JukeBoxText.color', getColorFromHex('FFFFFF'))
	
	--text for the song name
	makeLuaText('JukeBoxSubText', 'Insomniac', 350, -305-IntroTagWidth, 210)
	setTextAlignment('JukeBoxSubText', 'left')
	setObjectCamera('JukeBoxSubText', 'game')
	setTextSize('JukeBoxSubText', IntroSubTextSize)
	addLuaText('JukeBoxSubText')
	setProperty('JukeBoxSubText.color', getColorFromHex('FFFFFF'))
end

--motion functions
function onSongStart()
	-- Inst and Vocals start playing, songPosition = 0
	doTweenX('MoveInOne', 'JukeBoxTag', 0, 1, 'CircInOut')
	doTweenX('MoveInTwo', 'JukeBox', 0, 1, 'CircInOut')
	doTweenX('MoveInThree', 'JukeBoxText', 0, 1, 'CircInOut')
	doTweenX('MoveInFour', 'JukeBoxSubText', 0, 1, 'CircInOut')
	
	runTimer('JukeBoxWait', 6, 1)
end

function onTimerCompleted(tag, loops, loopsLeft)
	-- A loop from a timer you called has been completed, value "tag" is it's tag
	-- loops = how many loops it will have done when it ends completely
	-- loopsLeft = how many are remaining
	if tag == 'JukeBoxWait' then
		doTweenX('MoveOutOne', 'JukeBoxTag', -950, 1.5, 'CircInOut')
		doTweenX('MoveOutTwo', 'JukeBox', -950, 1.5, 'CircInOut')
		doTweenX('MoveOutThree', 'JukeBoxText', -950, 1.5, 'CircInOut')
		doTweenX('MoveOutFour', 'JukeBoxSubText', -950, 1.5, 'CircInOut')
	end
end