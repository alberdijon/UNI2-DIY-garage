/*
 * This software has been developed by Uni2
 * Under the GNU General Public License
 */
package model;

import java.util.ArrayList;
import javax.swing.table.AbstractTableModel;

/**
 *
 * @author agirrezabala.peru
 */
public class LowStockItemsTable extends AbstractTableModel {
    private ArrayList<LowStockItems> lsitem = new ArrayList<>();
    private final String[] columnName = {"ID", "Name", "Brand", "Stock"};
    
    public LowStockItemsTable(ArrayList<LowStockItems> lastStock){
        this.lsitem=lastStock;
    }

    @Override
    public int getRowCount() {
        return lsitem.size();
    }

    @Override
    public int getColumnCount() {
        return columnName.length;
    }
    public String getColumnName(int column){
        return columnName[column];
    }

    @Override
    public Object getValueAt(int rowIndex, int columnIndex) {
        
        switch(columnIndex){
            
            case 0: return lsitem.get(rowIndex).getId();
            case 1: return lsitem.get(rowIndex).getName();
            case 2: return lsitem.get(rowIndex).getBrand();
            case 3: return lsitem.get(rowIndex).getStock();

            default: return null;
        }
    }
    
}
