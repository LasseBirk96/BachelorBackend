


	INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('123', 'RS', 'Albus Dumbledore', 'ABEW');
    INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('654', 'AD', 'Severus Snape', 'SSPM');
    INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('875', 'CS', 'Minerva McGonagol', 'MMCG');
    INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('456', 'LD', 'Minerva McGonagol', 'MMCG');
        INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('324', 'ZD', 'Minerva McGonagol', 'MMCG');
    
	INSERT INTO BusinessGroup (Id, Name, ShortName) VALUES ('123', 'FL Smidth', 'FLS');
    INSERT INTO BusinessGroup (Id, Name, ShortName) VALUES ('345', 'Novo Nordisk', 'NOVO');
	
    INSERT INTO BusinessGroupResource (Id, BusinessGroupId, Type, Assigned, Consumed, Available, Reserved, RecordDateTime, RecordType) VALUES ('765', '123', 'thing', '10','10', '11','0', CURRENT_DATE, 'ORIGINAL');