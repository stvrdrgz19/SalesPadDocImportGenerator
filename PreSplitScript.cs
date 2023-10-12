//Split Sales Document > Pre Split Script
if (Genframe4.Utils.ConvertToInt64(sd.val_Sales_Doc_Num) % 2 == 0)
	sd.val_Combine_Split_Docs = true;
sd.Save();
return "";
