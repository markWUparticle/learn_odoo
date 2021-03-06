# -*- coding: utf-8 -*-

from odoo import _,models, fields, api



class Accessdate(models.Model):
    _inherit =  'ir.model'
    access_data=fields.Text(string='Accessdata')

    @api.multi
    def accessdata(self):
        def convert(x):
            if x is True:
                x = '1'
            else:
                x = '0'
            return x

        def convert_id(xml_ids):
            if xml_ids:
                for xml_id in xml_ids.values():
                    for id in xml_id:
                        return id
            return ''

        lists = []
        data=''
        for line in self:
            access_ids=line.access_ids
            for access in access_ids:
                # 得到模块权限表id

                access_xml_ids = models.Model._get_external_ids(access)     #得到权限表的外部ID
                xml_data = convert_id(access_xml_ids)                           #外部id取值
                if '.' in xml_data:
                    id = xml_data.split('.')[1].encode('utf-8')
                else:
                    id = xml_data.encode('utf-8')

                name=access.name.encode('utf-8')       #模块名

                model = access.model_id.model
                a=model.split('.')
                a='_'.join(a)
                model_id_id=('model_'+a).encode('utf-8')       #对应的对象模型

                group_xml_ids = models.Model._get_external_ids(access.group_id)
                group=convert_id(group_xml_ids).encode('utf-8')        #对应的组

                #得到模型增删改查权限
                perm_read=access.perm_read
                perm_write=access.perm_write
                perm_create=access.perm_create
                perm_unlink=access.perm_unlink

                perm_read=convert(perm_read)
                perm_write = convert(perm_write)
                perm_create = convert(perm_create)
                perm_unlink = convert(perm_unlink)

                list=[id,name,model_id_id,group,perm_read,perm_write,perm_create,perm_unlink]  #加入列表
                data = ",".join(list)                      #用,连接成字符串
                lists.append(data)
                data = "\n".join(lists)

            line.write({'access_data': data})   #写入字段

            form_id = self.env.ref('access_data.view_form_open_export_access_data').id
            return {
                    'name': _('Access Rights Data'),
                    'type': 'ir.actions.act_window',
                    'res_model': 'ir.model',
                    'view_mode': 'form',
                    'views': [(form_id, 'form')],
                    'res_id': line.id,
                    'target': 'new',
                    'flags': {'form': {'action_buttons': True}}
                    }



