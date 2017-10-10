from proto.compiled import bfo_pb2
import time

## This describes the typical way to construct Entities
examplebfo = bfo_pb2.Entity()
examplebfo.term = 'Object'
occ_entity = examplebfo.sub_entity.add();  occ_entity.term = 'Occurrent'
con_entity = examplebfo.sub_entity.add();  con_entity.term = 'Continuant'

## Level 1
con_entity_i = con_entity.sub_entity.add();  con_entity_i.term   = 'Independent Continuant'
con_entity_g = con_entity.sub_entity.add();  con_entity_g.term   = 'Generically dependent continuant'
con_entity_s = con_entity.sub_entity.add();  con_entity_s.term   = 'Specifically dependent continuant'

occ_entity_process               = occ_entity.sub_entity.add(); occ_entity_process.term               = 'Process'
occ_entity_process_boundary      = occ_entity.sub_entity.add(); occ_entity_process_boundary.term      = 'Process Boundary'
occ_entity_spatiotemporal_region = occ_entity.sub_entity.add(); occ_entity_spatiotemporal_region.term = 'Spatiotemporal region'
occ_entity_temporal_region       = occ_entity.sub_entity.add(); occ_entity_temporal_region.term       = 'Temporal region'

## Level 2
con_entity_i_m = con_entity_i.sub_entity.add();  con_entity_i_m.term   = 'Material entity' 
con_entity_i_i = con_entity_i.sub_entity.add();  con_entity_i_i.term   = 'Immaterial entity'

con_entity_s_r = con_entity_s.sub_entity.add();  con_entity_s_r.term   = 'Realizable entity'
con_entity_s_q = con_entity_s.sub_entity.add();  con_entity_s_q.term   = 'Quality'

occ_entity_process_history     = occ_entity_process.sub_entity.add();         occ_entity_process_history.term     = 'Process history'
occ_entity_temporal_region_0d  = occ_entity_temporal_region.sub_entity.add(); occ_entity_temporal_region_0d.term  = 'Temporal region 0d'
occ_entity_temporal_region_1d  = occ_entity_temporal_region.sub_entity.add(); occ_entity_temporal_region_1d.term  = 'Temporal region 1d'

## Level 3
con_entity_i_i_co = con_entity_i_i.sub_entity.add();  con_entity_i_i_co.term   = 'Continuant fiat boundary'
con_entity_i_i_si = con_entity_i_i.sub_entity.add();  con_entity_i_i_si.term   = 'Site'
con_entity_i_i_sp = con_entity_i_i.sub_entity.add();  con_entity_i_i_sp.term   = 'Spatial region'

con_entity_i_m_ob = con_entity_i_i.sub_entity.add();  con_entity_i_m_ob.term   = 'Object'
con_entity_i_m_fi = con_entity_i_i.sub_entity.add();  con_entity_i_m_fi.term   = 'Fiat object part'
con_entity_i_m_oa = con_entity_i_i.sub_entity.add();  con_entity_i_m_oa.term   = 'Object aggregate'

con_entity_s_q_r = con_entity_s_q.sub_entity.add();  con_entity_s_q_r.term   = 'Relational quality'
con_entity_s_r_r = con_entity_s_r.sub_entity.add();  con_entity_s_r_r.term   = 'Role'
con_entity_s_r_d = con_entity_s_r.sub_entity.add();  con_entity_s_r_d.term   = 'Disposition'

## Level 4
con_entity_i_i_co_1 = con_entity_i_i_co.sub_entity.add();  con_entity_i_i_co_1.term   = 'Continuant fiat boundary 1d'
con_entity_i_i_co_2 = con_entity_i_i_co.sub_entity.add();  con_entity_i_i_co_2.term   = 'Continuant fiat boundary 2d'
con_entity_i_i_co_3 = con_entity_i_i_co.sub_entity.add();  con_entity_i_i_co_3.term   = 'Continuant fiat boundary 3d'

con_entity_i_i_sp_0 = con_entity_i_i_sp.sub_entity.add();  con_entity_i_i_sp_0.term   = 'Spatial region 0d'
con_entity_i_i_sp_1 = con_entity_i_i_sp.sub_entity.add();  con_entity_i_i_sp_1.term   = 'Spatial region 1d'
con_entity_i_i_sp_2 = con_entity_i_i_sp.sub_entity.add();  con_entity_i_i_sp_2.term   = 'Spatial region 2d'
con_entity_i_i_sp_3 = con_entity_i_i_sp.sub_entity.add();  con_entity_i_i_sp_3.term   = 'Spatial region 3d'

