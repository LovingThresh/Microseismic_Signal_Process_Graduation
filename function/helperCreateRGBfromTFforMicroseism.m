function helperCreateRGBfromTFforMicroseism(signal,filename,label)

save_path = 'L:\dataset_for_graduation';
Fs = 10000;
signalLength = length(signal);

fb = cwtfilterbank('SignalLength',signalLength,'SamplingFrequency',Fs,'VoicesPerOctave',12);
[cfs,~] = wt(fb,signal);
cfs = abs(cfs);
im = ind2rgb(im2uint8(rescale(cfs)),jet(128));
imgLoc = fullfile(save_path,label);
imFileName = strcat(label,'_',filename,'.jpg');
imwrite(imresize(im,[224 224]),fullfile(imgLoc,imFileName));

end


